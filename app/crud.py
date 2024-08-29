from datetime import datetime
import requests
from sqlalchemy.orm import Session
from app.models import DataItem, SectionA, SectionB, SectionC
import json
from sqlalchemy.orm import joinedload


def get_all_items(db: Session):
    """
    Retrieve all records from the database.

    This function will return a list of all records in the database. It uses a
    single query to fetch all records, and then uses SQLAlchemy's joinedload
    option to fetch each record's section_a, section_b, and section_c in a single
    pass.

    :param db: The database session to use.
    :return: A list of DataItem objects, each with their section_a, section_b, and
        section_c attributes populated.
    """
    return (
        db.query(DataItem)
        .options(
            joinedload(DataItem.section_c),
            joinedload(DataItem.section_a),
            joinedload(DataItem.section_b),
        )
        .all()
    )


def create_record(
    db: Session,
    data_item: dict,
    section_a: dict,
    section_b: dict,
    section_c: dict,
):
    """
    Create a new record in the database.

    This function will create a new record in the database from the given
    dictionaries, and then save each record's section_a, section_b, and section_c
    in separate tables.

    :param db: The database session to use.
    :param data_item: The dictionary of values for the DataItem model.
    :param section_a: The dictionary of values for the SectionA model.
    :param section_b: The dictionary of values for the SectionB model.
    :param section_c: The dictionary of values for the SectionC model.
    :return: The dictionary of values for the DataItem model.
    """
    parent = DataItem(**data_item)
    db.add(parent)
    db.commit()
    db.refresh(parent)

    # Save form sections in separate tables
    db.add(SectionA(**section_a, parent_id=parent.id))
    db.add(SectionB(**section_b, parent_id=parent.id))
    db.add(SectionC(**section_c, parent_id=parent.id))
    db.commit()

    print("OK => Record saved in database")

    return data_item


def clean_data_item(payload: dict) -> dict:
    """
    Clean up a payload dictionary by performing the following operations:
    - Replacing / with _ in keys
    - Removing preceding __ from keys
    - Removing preceding _ from keys
    - Fixing the Version field
    - Encoding JSON fields
    - Formatting dates
    - Replacing primary key with external_id
    - Extracting sections into separate dictionaries

    :param payload: The dictionary to clean up
    :return: A dictionary with the cleaned up data
    """
    data = {}
    # Clean up data keys
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

    # Remove 'group_mx5fl16_' prefix from keys
    data = rename_prefix(data, "group_mx5fl16_")

    # Extract sections
    section_a = extract_fields_by_prefix(data, "sec_a_")
    section_b = extract_fields_by_prefix(data, "sec_b_")
    section_c = extract_fields_by_prefix(data, "sec_c_")

    return {
        "parent": {
            key: value for key, value in data.items() if not key.startswith("sec_")
        },
        "section_a": section_a,
        "section_b": section_b,
        "section_c": section_c,
    }


def extract_fields_by_prefix(data, prefix):
    """Extracts fields starting with a given prefix into a new dictionary.

    Args:
      data: The original dictionary.
      prefix: The prefix to filter fields by.

    Returns:
      A tuple containing two dictionaries:
        - The original dictionary with fields starting with the prefix removed.
        - A new dictionary containing only the fields that started with the prefix.
    """
    extracted_data = {}
    remaining_data = {}

    for key, value in data.items():
        if key.startswith(prefix):
            extracted_data[key] = value
        else:
            remaining_data[key] = value

    return extracted_data


def fetch_data_from_kobo() -> dict:
    """
    Fetches data from the KoBoToolbox API.

    Returns:
        The response JSON parsed as a Python dictionary.
    """
    url = "https://kf.kobotoolbox.org/api/v2/assets/aW9w8jHjn4Cj8SSQ5VcojK/data.json"
    payload = ""
    headers = {
        "Authorization": "Token f24b97a52f76779e97b0c10f80406af5e9590eaf",
        "Cookie": "django_language=en",
    }
    response = requests.get(url, headers=headers, data=payload)
    return json.loads(response.text)


def rename_prefix(data, prefix):
    new_data = {}
    for key, value in data.items():
        if key.startswith(prefix):
            new_key = key.replace(prefix, "")
            new_data[new_key] = value
        else:
            new_data[key] = value
    return new_data
