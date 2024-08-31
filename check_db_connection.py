from fixture.orm import SQLAlchemyFixture
from model.group import Group

db = SQLAlchemyFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts_in_group = db.get_contacts_not_in_group(Group(group_id="147"))
    for contact in contacts_in_group:
        print(contact)
    print(len(contacts_in_group))
finally:
    pass
