from model.contact import Contact
from random import randrange
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Kirill", lastname="Seleznev"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    update_contact = Contact(firstname="Robert")
    update_contact.id = contact.id
    update_contact.lastname = contact.lastname
    app.contact.modify_contact_by_id(contact.id, update_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(update_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
