from typing import Dict, List


def contact_schema(contact) -> Dict:
    return {"id": str(contact["_id"]),
            "name": contact["name"],
            "email": contact["email"],
            "message": contact["message"]}


def contacts_schema(contacts) -> List:
    return [contact_schema(contact) for contact in contacts]
