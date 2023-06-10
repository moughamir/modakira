from models.contact import Contact


def generate_vcard(contact: Contact) -> str:
    vcard = f"BEGIN:VCARD\nVERSION:3.0\n"
    vcard += f"N:{contact.last_name};{contact.first_name};;;\n"
    vcard += "END:VCARD\n\ı"
    return vcard
