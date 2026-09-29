"""
Pydantic schemas for structured records — matches the Data Schemas section
of the architecture blueprint doc. Session 0 plumbing: written for you so
loaders.py and tagging.py have something concrete to import.
"""
from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel


class IdentityRecord(BaseModel):
    document_type: Literal["identity"] = "identity"
    sub_type: Literal["PAN", "Aadhaar", "Passport", "DrivingLicense"]
    sensitivity_level: Literal["strictly_confidential"] = "strictly_confidential"
    id_number: str  # encrypt at rest before persisting
    full_name: str
    issue_date: date
    expiry_date: Optional[date] = None
    issuing_authority: str
    source_file: str


class AcademicRecord(BaseModel):
    document_type: Literal["academic"] = "academic"
    sensitivity_level: Literal["private"] = "private"
    institution: str
    degree: str
    field_of_study: str
    start_date: date
    end_date: Optional[date] = None
    favorite_subjects: list[str] = []
    weak_areas: list[str] = []
    self_improvement_targets: list[str] = []
    source_file: str


class FinancialRecord(BaseModel):
    document_type: Literal["financial"] = "financial"
    sub_type: Literal["payslip", "tax_filing", "compensation_summary"]
    sensitivity_level: Literal["strictly_confidential"] = "strictly_confidential"
    period: str  # "YYYY-MM"
    gross_amount: float
    net_amount: float
    currency: str = "INR"
    employer: str
    source_file: str
