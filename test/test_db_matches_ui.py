from model.group import Group
from model.contact import Contact
import re


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_raw_list = db.get_group_list()

    def clean(group):
        cleaned_name = re.sub(r'\s+', ' ', group.group_name.strip())
        return Group(group_id=group.group_id, group_name=cleaned_name)
    db_list = list(map(clean, db_raw_list))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_raw_list = db.get_contact_list()

    def clean(contact):
        return Contact(
            id=contact.id,
            lastname=contact.lastname.strip(),
            firstname=contact.firstname.strip()
        )
    db_list = list(map(clean, db_raw_list))
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
