from model.contact import Contact
from random import randrange


def test_modify_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Kirill", lastname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobilephone="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmonth="April", byear="1996"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Dasha")
    contact.contact_id = old_contacts[index].contact_id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
