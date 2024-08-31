import random
import time
from model.group import Group
from model.contact import Contact


def test_remove_contact_from_group(app, orm):
    groups_with_contacts = [group for group in orm.get_group_list() if orm.get_contacts_in_group(group)]
    if not groups_with_contacts:
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(group_name="qweqwe", group_header="qweqwe", group_footer="qweqwe"))
        contacts_not_in_groups = orm.get_contacts_not_in_any_group()
        if not contacts_not_in_groups:
            app.contact.creating(Contact(firstname="qwe", lastname="qwe", mobilephone="666666"))
            contacts_not_in_groups = orm.get_contacts_not_in_any_group()
        assert contacts_not_in_groups
        random_contact = random.choice(contacts_not_in_groups)
        random_contact_id = random_contact.id
        random_group = random.choice(orm.get_group_list())
        random_group_id = random_group.group_id
        app.contact.open_contacts_without_groups()
        app.contact.add_contact_to_group(random_contact_id, random_group_id)
        contacts_in_group = orm.get_contacts_in_group(random_group)
        assert any(c.id == random_contact_id for c in contacts_in_group)
        groups_with_contacts = [group for group in orm.get_group_list() if orm.get_contacts_in_group(group)]
    assert groups_with_contacts
    random_group = random.choice(groups_with_contacts)
    contacts_in_group = orm.get_contacts_in_group(random_group)
    assert contacts_in_group
    random_contact = random.choice(contacts_in_group)
    random_contact_id = random_contact.id
    app.contact.remove_from_group(random_contact_id, random_group.group_id)

    def contact_is_removed():
        contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
        return any(c.id == random_contact_id for c in contacts_not_in_group)
    for _ in range(5):
        if contact_is_removed():
            break
        time.sleep(2)
    else:
        assert False
