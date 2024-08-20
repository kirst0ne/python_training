from model.group import Group


def test_modify_first_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="New group")
    if app.group.count() == 0:
        app.group.create(group)
        old_groups = app.group.get_group_list()
    group.group_id = old_groups[0].group_id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    old_groups_with_id = sorted([g for g in old_groups if g.group_id is not None], key=Group.id_or_max)
    new_groups_with_id = sorted([g for g in new_groups if g.group_id is not None], key=Group.id_or_max)
    assert len(old_groups_with_id) == len(new_groups_with_id)
    if old_groups_with_id:
        old_groups_with_id[0] = group
    assert old_groups_with_id == new_groups_with_id


def test_modify_first_group_header(app):
    old_groups = app.group.get_group_list()
    group = Group(group_header="New header")
    if app.group.count() == 0:
        app.group.create(group)
        old_groups = app.group.get_group_list()
    group.group_id = old_groups[0].group_id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    old_groups_with_id = sorted([g for g in old_groups if g.group_id is not None], key=Group.id_or_max)
    new_groups_with_id = sorted([g for g in new_groups if g.group_id is not None], key=Group.id_or_max)
    assert len(old_groups_with_id) == len(new_groups_with_id)
    if old_groups_with_id:
        old_groups_with_id[0] = group
    assert old_groups_with_id == new_groups_with_id
