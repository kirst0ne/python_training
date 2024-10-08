from model.group import Group
from random import randrange
import random


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="New group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    update_group = Group(group_name="New group")
    update_group.group_id = group.group_id
    app.group.modify_group_by_id(group.group_id, update_group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(update_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_first_group_header(app):
#    old_groups = app.group.get_group_list()
#    group = Group(group_header="New header")
#    if app.group.count() == 0:
#        app.group.create(group)
#        old_groups = app.group.get_group_list()
#    group.group_id = old_groups[0].group_id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    old_groups_with_id = sorted([g for g in old_groups if g.group_id is not None], key=Group.id_or_max)
#    new_groups_with_id = sorted([g for g in new_groups if g.group_id is not None], key=Group.id_or_max)
#    assert len(old_groups_with_id) == len(new_groups_with_id)
#    if old_groups_with_id:
#        old_groups_with_id[0] = group
#    assert old_groups_with_id == new_groups_with_id
