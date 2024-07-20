from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(group_name="New group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="test"))
    app.group.modify_first_group(Group(group_header="New header"))
