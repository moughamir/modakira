from typing import List
from pydantic import BaseModel

from models import PhoneNumber, Email, Address, URL


class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_numbers: List[PhoneNumber]
    emails: List[Email]
    addresses: List[Address]
    urls: List[URL]
    company: str
    notes: str
    is_professional: bool
