from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Kirill", lastname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobile="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmonth="April", byear="1996"))
    app.contact.modify_first_contact(Contact(firstname="Grezckii", lastname="Oleg", middlename="Viktorovich",
                                             nickname="oreh666", address="Vokzalnya st. 17, 49 flat",
                                             mobile="+79116660066", email="emaple@yandex.ru", bday="6",
                                             bmonth="January", byear="1998"))
