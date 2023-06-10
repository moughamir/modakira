from pydantic import BaseModel

class PhoneNumber(BaseModel):
    number: int
    label: str
