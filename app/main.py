from typing import Union
from fastapi import FastAPI, Request
import requests
import json

from .models import DataItem

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Wor"}


@app.post("/register_webhook")
def register_url():
    url = "http://dev.inkomoko.com:1055/register_webhook"
    # payload = json.dumps({"url": "https://inkomoko.loca.lt/api"})
    payload = json.dumps({"url": "https://inkomoko.requestcatcher.com/test"})
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=payload)
    return json.loads(response.text)


@app.get("/sample_data")
def sample_data():
    url = "https://kf.kobotoolbox.org/api/v2/assets/aW9w8jHjn4Cj8SSQ5VcojK/data.json"
    payload = ""
    headers = {
        "Authorization": "Token f24b97a52f76779e97b0c10f80406af5e9590eaf",
        "Cookie": "django_language=en",
    }
    response = requests.get(url, headers=headers, data=payload)
    return json.loads(response.text)


@app.post("/process_webhook")
async def process_webhook(request: Request):
    payload = await request.body()
    payload = format_data_keys(json.loads(payload))

    # Convert payload to DataItem
    try:
        data_item = DataItem(**payload)
    except Exception as e:
        return {"error": str(e)}

    return data_item


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

    return data
