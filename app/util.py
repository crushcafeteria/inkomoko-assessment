from app.models import DataItem
import time


def save_record(db, data_item: DataItem):
    db.add(data_item)
    db.commit()
    db.refresh(data_item)
    print("Record saved in database")

    return data_item
