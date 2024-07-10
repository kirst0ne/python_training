# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Kirill", secondname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobile_phone="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmounth="April", byear="1996"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", secondname="", middlename="", nickname="", address="",
                               mobile_phone="", email="", bday="", bmounth="-", byear=""))
    app.session.logout()
