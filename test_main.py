from fastapi import BackgroundTasks
from fastapi.testclient import TestClient
import pytest
from app import crud
from app.main import app  # assuming this code is in a file called main.py
import json

REQUEST_PAYLOAD = """
{
  "_id": 376087072,
  "formhub/uuid": "a7eb959ada4c485b8334ee761ab1e4a7",
  "starttime": "2024-08-27T11:06:06.920+03:00",
  "endtime": "2024-08-27T11:18:01.224+03:00",
  "cd_survey_date": "2024-08-27",
  "sec_a/unique_id": "SS01406240716104310",
  "sec_a/cd_biz_country_name": "Kenya",
  "sec_a/cd_biz_region_name": "Dadaab",
  "sec_b/bda_name": "Yunis Abdirahman",
  "sec_b/cd_cohort": "Cohort 2",
  "sec_b/cd_program": "Livelihood",
  "sec_c/cd_client_name": "ESPERANCE NYEYIMANA",
  "sec_c/cd_client_id_manifest": "106-00011657",
  "sec_c/cd_location": "Juba urban refugees",
  "sec_c/cd_clients_phone": "926985823",
  "sec_c/cd_phoneno_alt_number": "980326248",
  "sec_c/cd_clients_phone_smart_feature": "Smart phone Feature phone",
  "sec_c/cd_gender": "Female",
  "sec_c/cd_age": "28",
  "sec_c/cd_nationality": "Burundian",
  "sec_c/cd_strata": "Urban Based Refugee",
  "sec_c/cd_disability": "No",
  "sec_c/cd_education": "Finished high school/Graduate",
  "sec_c/cd_client_status": "New clients",
  "sec_c/cd_sole_income_earner": "Yes",
  "sec_c/cd_howrespble_pple": "4",
  "group_mx5fl16/cd_biz_status": "Idea stage",
  "__version__": "vBfco72yRxvHQun3cF8HPK",
  "meta/instanceID": "uuid:eb336e5a-d988-4933-ad07-08d64ffbb115",
  "_xform_id_string": "aW9w8jHjn4Cj8SSQ5VcojK",
  "_uuid": "eb336e5a-d988-4933-ad07-08d64ffbb115",
  "_attachments": [],
  "_status": "submitted_via_web",
  "_geolocation": [
    null,
    null
  ],
  "_submission_time": "2024-08-27T08:18:02",
  "_tags": [],
  "_notes": [],
  "_validation_status": {},
  "_submitted_by": null
}
"""


client = TestClient(app)


def test_redirect():
    response = client.get("/")
    assert response.status_code == 200


def test_dataset():
    response = client.get("/dataset")
    assert response.status_code == 200


def test_extract_data_from_kobo():
    response = client.get("/sample_data")
    assert response.status_code == 200


def test_process_webhook():
    client = TestClient(app)

    response = client.post("/process_webhook", data=REQUEST_PAYLOAD)

    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}"

    expected_msg = {
        "status": "OK",
        "msg": "Record successfully received for processing...",
    }

    assert (
        response.json() == expected_msg
    ), f"Expected {expected_msg} but got {response.json()}"
