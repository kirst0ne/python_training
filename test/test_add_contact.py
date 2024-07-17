# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Kirill", lastname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobile="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmonth="April", byear="1996"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", middlename="", nickname="", address="",
                               mobile="", email="", bday="", bmonth="-", byear=""))
