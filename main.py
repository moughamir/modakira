from fastapi import FastAPI
from models import Contact

app = FastAPI()

# in-memory storage mechnism
contacts = []


@app.get("/contacts")
def get_contacts():
    return contacts


@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    for contact in contacts:
        if contact.id == contact_id:
            return contact
        return {"status": 404, "message": "Contact Not Found."}


@app.post("/contacts")
def create_contact(contact: Contact):
    contacts.append(contact)
    return contact


@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    for idx, stored_contact in enumerate(contacts):
        if stored_contact.id == contact_id:
            contacts[idx] = contact
            return {"status": 202, "message": "Contact updated"}
    return {"status": 404, "message": "Contact not found"}


@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    for idx, stored_contact in enumerate(contacts):
        if stored_contact.id == contact_id:
            contacts.pop(idx)
            return {"status": 200, "message": "Contact Deleted"}
    return {"status": 404, "message": "Contact not Deleted for unknown reasons"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=1337)
