from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, HttpUrl

from app.schema.enum import Gender


class UserAuthEmailModel(BaseModel):
    email: EmailStr
    photo_url: HttpUrl
    display_name: str


class UserModelSchema(BaseModel):
    phone_number: Optional[str] = Field(default=None, min_length=11, max_length=13,examples=['0919---752 or +98919----752 / null'])
    name: Optional[str] = Field(default=None, min_length=3, max_length=70,examples=['str / null'])
    last_name: Optional[str] = Field(default=None, min_length=3, max_length=100,examples=['str / null'])
    display_name: Optional[str] = Field(default=None, min_length=3, max_length=70,examples=['str / '])
    gender: Optional[Gender] = Field(default=None,examples=['male/female/other/not_given / null'])
    age: Optional[int] = Field(default=None,examples=['15 < int < 120 / null'])
    country: Optional[str] = Field(default=None,examples=['str / null'])
