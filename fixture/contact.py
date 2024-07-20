from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init create contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.open_contact_page()

    def fill_contact_form(self, contact):
        self.change_field_contact_value("firstname", contact.firstname)
        self.change_field_contact_value("lastname", contact.lastname)
        self.change_field_contact_value("middlename", contact.middlename)
        self.change_field_contact_value("nickname", contact.nickname)
        self.change_field_contact_value("address", contact.address)
        self.change_field_contact_value("mobile", contact.mobile)
        self.change_field_contact_value("email", contact.email)
        self.change_field_contact_value("bday", contact.bday, is_dropdown=True)
        self.change_field_contact_value("bmonth", contact.bmonth, is_dropdown=True)
        self.change_field_contact_value("byear", contact.byear)

    def change_field_contact_value(self, field_name, text, is_dropdown=False):
        wd = self.app.wd
        if text is not None:
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.NAME, field_name))
            )
            element.click()
            if is_dropdown:
                select = Select(element)
                select.select_by_visible_text(text)
            else:
                element.clear()
                element.send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init modify contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # modify contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.open_contact_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.execute_script("window.scrollBy(0, 800);")
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))
