from model.group import Group


def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="New group"))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_header="New header"))
    app.session.logout()
