from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.session.home_page()
    app.contact.modify_first_contact(Contact(firstname="Grezckii", secondname="Oleg", middlename="Viktorovich",
                               nickname="oreh666", address="Vokzalnya st. 17, 49 flat",
                               mobile_phone="+79116660066", email="emaple@yandex.ru", bday="6",
                               bmounth="January", byear="1998"))
    app.session.logout()
