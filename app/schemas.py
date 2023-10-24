from pydantic import BaseModel, Field
from datetime import datetime

class Student(BaseModel):
    name: str = Field(...)
    roll_no: str = Field(...)
    phone_number: int = Field(...)
    is_active: bool = Field(default=True)

class StudentResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    roll_no: str = Field(...)
    phone_number: int = Field(...)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(...)