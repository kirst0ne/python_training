from model.contact import Contact
import random
from random import randrange
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


def handle_alert_if_present(driver):
    try:
        alert = Alert(driver)
        alert.accept()
    except NoAlertPresentException:
        pass


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Kirill", lastname="Seleznev", middlename="Aleksandrovich",
                               nickname="kirts0ne", address="Repischeva st. 10, 149 flat",
                               mobilephone="+79119715279", email="okolo66@yandex.ru", bday="30",
                               bmonth="April", byear="1996"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
