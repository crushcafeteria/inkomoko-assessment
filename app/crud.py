from sqlalchemy.orm import Session

from app.models import DataItem


def get_all_items(db: Session):
    return db.query(DataItem).all()


def create_record(db: Session, data_item: DataItem):
    db.add(data_item)
    db.commit()
    db.refresh(data_item)
    print("Record saved in database")

    return data_item
