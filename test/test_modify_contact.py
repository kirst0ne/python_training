from model.contact import Contact


def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Kirill", lastname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobile="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmonth="April", byear="1996")
    if app.contact.count() == 0:
        app.contact.create(contact)
        old_contacts = app.contact.get_contact_list()
    # Логирование для отладки
    print(f"Old Contacts: {old_contacts}")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    # Логирование для отладки
    print(f"New Contacts: {new_contacts}")
    old_contact_with_id = sorted([c for c in old_contacts if c.contact_id is not None], key=Contact.id_or_max)
    new_contact_with_id = sorted([c for c in new_contacts if c.contact_id is not None], key=Contact.id_or_max)
    # Сравнение списков с логированием
    print(f"Old Contact with ID: {old_contact_with_id}")
    print(f"New Contact with ID: {new_contact_with_id}")
    assert len(old_contact_with_id) == len(new_contact_with_id)
    if old_contact_with_id:
        old_contact_with_id[0] = contact
    assert old_contact_with_id == new_contact_with_id
