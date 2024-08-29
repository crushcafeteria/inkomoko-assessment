from sqlalchemy import ARRAY, JSON, Column, DateTime, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class DataItem(Base):
    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer)
    formhub_uuid = Column(String(254))
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    cd_survey_date = Column(String(254))
    group_mx5fl16_cd_biz_status = Column(String(254))
    version = Column(String(254))
    meta_instanceID = Column(String(254))
    xform_id_string = Column(String(254))
    uuid = Column(String(254))  # Or UUID if using PostgreSQL: UUID(as_uuid=True)
    attachments = Column(String(254))  # Or JSON if your database supports it
    status = Column(String(254))
    geolocation = Column(JSON)  # Store as JSON for flexibility
    submission_time = Column(DateTime)
    tags = Column(String(254))  # Or JSON
    notes = Column(String(254))  # Or JSON
    validation_status = Column(JSON)
    submitted_by = Column(String(254))

    section_a = relationship("SectionA", backref="dataset")
    # section_b = relationship("SectionB", backref="dataset")
    # section_c = relationship("SectionC", backref="dataset")


class SectionA(Base):
    __tablename__ = "section_a"

    id = Column(Integer, primary_key=True, index=True)
    sec_a_unique_id = Column(String(254))
    sec_a_cd_biz_country_name = Column(String(254))
    sec_a_cd_biz_region_name = Column(String(254))
    parent_id = Column(Integer, ForeignKey("dataset.id"))


class SectionB(Base):
    __tablename__ = "section_b"

    id = Column(Integer, primary_key=True, index=True)
    sec_b_bda_name = Column(String(254))
    sec_b_cd_cohort = Column(String(254))
    sec_b_cd_program = Column(String(254))
    parent_id = Column(Integer, ForeignKey("dataset.id"))


class SectionC(Base):
    __tablename__ = "section_c"

    id = Column(Integer, primary_key=True, index=True)
    sec_c_cd_client_name = Column(String(254))
    sec_c_cd_client_id_manifest = Column(String(254))
    sec_c_cd_location = Column(String(254))
    sec_c_cd_clients_phone = Column(String(254))
    sec_c_cd_phoneno_alt_number = Column(String(254))
    sec_c_cd_clients_phone_smart_feature = Column(String(254))
    sec_c_cd_gender = Column(String(254))
    sec_c_cd_age = Column(Integer)
    sec_c_cd_nationality = Column(String(254))
    sec_c_cd_strata = Column(String(254))
    sec_c_cd_disability = Column(String(254))
    sec_c_cd_education = Column(String(254))
    sec_c_cd_client_status = Column(String(254))
    sec_c_cd_sole_income_earner = Column(String(254))
    sec_c_cd_howrespble_pple = Column(Integer)
    parent_id = Column(Integer, ForeignKey("dataset.id"))
