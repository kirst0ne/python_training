from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
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

        ##wd.find_element_by_name("firstname").click()
        ##wd.find_element_by_name("firstname").clear()
        ##wd.find_element_by_name("firstname").send_keys(contact.firstname)
        ##wd.find_element_by_name("lastname").click()
        ##wd.find_element_by_name("lastname").clear()
        ##wd.find_element_by_name("lastname").send_keys(contact.lastname)
        ##wd.find_element_by_name("middlename").click()
        ##wd.find_element_by_name("middlename").clear()
        ##wd.find_element_by_name("middlename").send_keys(contact.middlename)
        ##wd.find_element_by_name("nickname").click()
        ##wd.find_element_by_name("nickname").clear()
        ##wd.find_element_by_name("nickname").send_keys(contact.nickname)
        ##wd.find_element_by_name("address").click()
        ##wd.find_element_by_name("address").clear()
        ##wd.find_element_by_name("address").send_keys(contact.address)
        ##wd.find_element_by_name("mobile").click()
        ##wd.find_element_by_name("mobile").clear()
        ##wd.find_element_by_name("mobile").send_keys(contact.mobile)
        ##wd.find_element_by_name("email").click()
        ##wd.find_element_by_name("email").clear()
        ##wd.find_element_by_name("email").send_keys(contact.email)
        ##wd.find_element_by_name("bday").click()
        ##Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        ##wd.find_element_by_name("bmonth").click()
        ##Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmounth)
        ##wd.find_element_by_name("byear").click()
        ##wd.find_element_by_name("byear").clear()
        ##wd.find_element_by_name("byear").send_keys(contact.byear)