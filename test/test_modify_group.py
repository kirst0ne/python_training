from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="GroupModify123", group_header="GroupModify123", group_footer="GroupModify123"))
    app.session.logout()
