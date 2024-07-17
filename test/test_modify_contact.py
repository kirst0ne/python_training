from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Grezckii", lastname="Oleg", middlename="Viktorovich",
                                             nickname="oreh666", address="Vokzalnya st. 17, 49 flat",
                                             mobile="+79116660066", email="emaple@yandex.ru", bday="6",
                                             bmonth="January", byear="1998"))
