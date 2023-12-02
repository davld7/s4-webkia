from pydantic import BaseModel
from typing import Optional


class ContactToCreate(BaseModel):
    name: str
    email: str
    message: str


class Contact(BaseModel):
    id: Optional[str]
    name: str
    email: str
    message: str
