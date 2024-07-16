from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.session.home_page()
    app.contact.modify_first_contact(Contact(firstname="Grezckii"))
    app.session.logout()


def test_modify_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.session.home_page()
    app.contact.modify_first_contact(Contact(email="exampe666@mail.ru"))
    app.session.logout()
