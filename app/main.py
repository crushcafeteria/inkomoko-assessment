from datetime import datetime
import time
from typing import Any
from fastapi import FastAPI, Request, Depends, BackgroundTasks
import requests, json
from .util import save_record
from .models import DataItem
from .database import engine, Base, SessionLocal
from sqlalchemy.orm import Session
from .schemas import DataItemSchema

app = FastAPI()

# Migrate database
time.sleep(5)
Base.metadata.create_all(bind=engine)


# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/dataset", summary="Show all data in the database")
def database_contents(db: Session = Depends(get_db)):
    dataset = db.query(DataItem).all()
    return dataset


@app.post("/register_webhook", summary="Register webhook URL")
def register_url():
    url = "http://dev.inkomoko.com:1055/register_webhook"

    payload = json.dumps({"url": "https://inkomoko.loca.lt/process_webhook"})
    # payload = json.dumps({"url": "https://inkomoko.requestcatcher.com/test"})

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=payload)
    return json.loads(response.text)


@app.get("/sample_data", summary="Preview some sample data")
def sample_data():
    url = "https://kf.kobotoolbox.org/api/v2/assets/aW9w8jHjn4Cj8SSQ5VcojK/data.json"
    payload = ""
    headers = {
        "Authorization": "Token f24b97a52f76779e97b0c10f80406af5e9590eaf",
        "Cookie": "django_language=en",
    }
    response = requests.get(url, headers=headers, data=payload)
    return json.loads(response.text)


@app.post("/process_webhook", summary="Receive data via webhook")
async def process_webhook(
    request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
) -> Any:
    # Prepare payload
    payload: dict = await request.body()
    payload = format_data_keys(json.loads(payload))

    try:
        # Build data model from data
        data_item = DataItem(**payload)

        # Save record in background task
        # Prevent blocking main thread
        background_tasks.add_task(save_record, db, data_item)

        return {
            "status": "OK",
            "msg": "Record successfully received. Processing in the background.",
        }

    except Exception as e:
        return {"error": str(e)}


def format_data_keys(payload: dict) -> dict:
    """
    Format the keys in the given data dictionary by replacing '/' with '_' and
    removing any leading and ending '_' and '__.

    Args:
        payload (dict): The dictionary to be formatted

    Returns:
        dict: The formatted dictionary
    """

    data = {}
    for key, value in payload.items():
        # Replace the / with _ in the key
        new_key: str = key.replace("/", "_")

        # Remove preceding __
        if new_key.startswith("__"):
            new_key = key[2:]

        # Remove preceding _
        if new_key.startswith("_"):
            new_key = key[1:]

        # Fix Version field
        if new_key == "version__":
            new_key = "version"

        # Assemble data with corrected key
        data[new_key] = value

    # Encode JSON fields
    data["attachments"] = json.dumps(data["attachments"])
    data["geolocation"] = json.dumps(data["geolocation"])
    data["tags"] = json.dumps(data["tags"])
    data["notes"] = json.dumps(data["notes"])
    data["validation_status"] = json.dumps(data["validation_status"])

    # Format dates
    data["starttime"] = datetime.fromisoformat(data["starttime"])
    data["endtime"] = datetime.fromisoformat(data["endtime"])

    # Replace primary key with external_id
    data["external_id"] = data.pop("id")

    return data
