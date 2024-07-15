from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="GroupModify123", group_header="Group123", group_footer="Group123"))
    app.session.logout()
