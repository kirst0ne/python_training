from model.group import Group


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(group_name="New group"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(group_header="New header"))
