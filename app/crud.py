from datetime import datetime
from sqlalchemy.orm import Session
from app.models import DataItem, SectionA, SectionB, SectionC
import json


def get_all_items(db: Session):
    return db.query(DataItem).all()


def create_record(
    db: Session,
    data_item: dict,
    section_a: dict,
    section_b: dict,
    section_c: dict,
):
    parent = DataItem(**data_item)
    db.add(parent)
    db.commit()
    db.refresh(parent)

    # Save sections
    db.add(SectionA(**section_a, parent_id=parent.id))
    db.add(SectionB(**section_b, parent_id=parent.id))
    db.add(SectionC(**section_c, parent_id=parent.id))
    db.commit()

    print("Record saved in database")

    return data_item


def clean_data_item(payload: dict) -> dict:
    """
    Format the keys in the given data dictionary by replacing '/' with '_' and
    removing any leading and ending '_' and '__.

    Args:
        payload (dict): The dictionary to be formatted

    Returns:
        dict: The formatted dictionary
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
