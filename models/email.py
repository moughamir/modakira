from pydantic import BaseModel


class Email(BaseModel):
    address: str
    label: str
