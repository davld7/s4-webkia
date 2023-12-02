from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse
from typing import List
from backend.database.models.contact import ContactToCreate, Contact
from backend.database.schemas.contact import contact_schema, contacts_schema
from backend.database.client import contacts_collection


prefix = "/contact"
tags = ["Contact"]

router = APIRouter(prefix=prefix, tags=tags)


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def contact() -> FileResponse:
    path = "templates/contact.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@router.get("/db", response_model=List[Contact])
async def get_contacts():
    return contacts_schema(contacts_collection.find())


@router.post("/db", response_model=Contact, status_code=status.HTTP_201_CREATED)
async def create_contact(contact: ContactToCreate):
    contact_data = contact.model_dump(exclude={"id"})
    result = contacts_collection.insert_one(contact_data)
    created_contact = contacts_collection.find_one({"_id": result.inserted_id})
    return contact_schema(created_contact)
