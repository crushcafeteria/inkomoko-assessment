from pydantic import Field, BaseModel
from .database import Base
from typing import List, Optional, Any
from datetime import datetime


class SectionASchema(BaseModel):
    id: Optional[int]
    sec_a_unique_id: str
    sec_a_cd_biz_country_name: str
    sec_a_cd_biz_region_name: str
    parent_id: int

    class Config:
        orm_mode = True


class SectionBSchema(BaseModel):
    id: Optional[int]
    sec_b_bda_name: str
    sec_b_cd_cohort: str
    sec_b_cd_program: str
    parent_id: int

    class Config:
        orm_mode = True


class SectionCSchema(BaseModel):
    id: Optional[int]
    sec_c_cd_client_name: str
    sec_c_cd_client_id_manifest: str
    sec_c_cd_location: str
    sec_c_cd_clients_phone: str
    sec_c_cd_phoneno_alt_number: str
    sec_c_cd_clients_phone_smart_feature: str
    sec_c_cd_gender: str
    sec_c_cd_age: int
    sec_c_cd_nationality: str
    sec_c_cd_strata: str
    sec_c_cd_disability: str
    sec_c_cd_education: str
    sec_c_cd_client_status: str
    sec_c_cd_sole_income_earner: str
    sec_c_cd_howrespble_pple: int
    parent_id: int

    class Config:
        orm_mode = True


class DataItemSchema(BaseModel):
    id: Optional[int]
    external_id: int
    formhub_uuid: str
    starttime: datetime
    endtime: datetime
    cd_survey_date: str
    cd_biz_status: str
    bd_biz_operating: str
    version: str
    meta_instanceID: str
    xform_id_string: str
    uuid: str
    attachments: str
    status: str
    geolocation: str
    submission_time: datetime
    tags: str
    notes: str
    validation_status: dict
    submitted_by: Optional[str] = None
    section_a: SectionASchema
    section_b: SectionBSchema
    section_c: SectionCSchema

    class Config:
        orm_mode = True
