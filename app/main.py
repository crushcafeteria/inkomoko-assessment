from datetime import datetime
import time
from typing import Any
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from starlette.responses import RedirectResponse
import requests, json
from app.crud import clean_data_item, fetch_data_from_kobo
from .models import DataItem, SectionA, SectionB, SectionC
from .database import engine, Base
from .dependencies import get_db
from . import crud
from sqlalchemy.orm import Session

app = FastAPI()

# Migrate database
time.sleep(5)
Base.metadata.create_all(bind=engine)


@app.get("/")
async def redirect():
    response = RedirectResponse(url="/dataset")
    return response


@app.get("/dataset", summary="Show all data in the database")
def database_contents(db: Session = Depends(get_db)):
    return crud.get_all_items(db)


@app.post("/register_webhook", summary="Register webhook URL")
def register_url(webhook_url: str = "http://172.104.118.166:8000/process_webhook"):
    url = "http://dev.inkomoko.com:1055/register_webhook"
    payload = json.dumps({"url": webhook_url})

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=payload)
    return json.loads(response.text)


@app.get("/sample_data", summary="Preview some sample data")
def sample_data():
    return fetch_data_from_kobo()


@app.post("/process_webhook", summary="Receive data via webhook")
async def process_webhook(
    request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
) -> Any:
    # Prepare payload
    payload: dict = await request.body()
    payload = crud.clean_data_item(json.loads(payload))

    try:
        # Save record in background task
        # Prevent blocking main thread
        background_tasks.add_task(
            crud.create_record,
            db,
            payload["parent"],
            payload["section_a"],
            payload["section_b"],
            payload["section_c"],
        )

        return {
            "status": "OK",
            "msg": "Record successfully received. Processing in the background.",
        }

    except Exception as e:
        return {"error": str(e)}


@app.get("/extract_records", response_description="Extract records from JSON endpoint")
def extract_records(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    records = fetch_data_from_kobo()

    for row in records["results"]:
        try:
            # Clean each data row
            payload = crud.clean_data_item(row)

            # Save record in background task
            # Prevent blocking main thread
            background_tasks.add_task(
                crud.create_record,
                db,
                payload["parent"],
                payload["section_a"],
                payload["section_b"],
                payload["section_c"],
            )

            print(
                f"MESSAGE => Successfully queued {payload['parent']['external_id']} for saving..."
            )

        except Exception as e:
            return {"error": str(e)}

    return {
        "status": "OK",
        "msg": "Record successfully received. Processing in the background.",
    }
