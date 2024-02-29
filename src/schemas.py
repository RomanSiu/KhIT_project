from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime

PhoneNumber.phone_format = "E164"


class ContactModel(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    surname: str = Field(min_lenght=3, max_length=30)
    email: EmailStr = Field(default=None)
    phone: PhoneNumber = Field(default=None)
    address: str = Field(max_length=100, default=None)
    birthday: datetime = Field()