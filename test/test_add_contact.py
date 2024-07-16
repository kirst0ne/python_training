# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Kirill", secondname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobile_phone="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmounth="April", byear="1996"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", secondname="", middlename="", nickname="", address="",
                               mobile_phone="", email="", bday="", bmounth="-", byear=""))
