from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Kirill", lastname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobile="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmonth="April", byear="1996"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Robert")
    contact.contact_id = old_contacts[0].contact_id
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
