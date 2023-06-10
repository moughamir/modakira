from models import Country
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    country: Country
    label: str
