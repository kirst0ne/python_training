from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_contact_value("firstname", contact.firstname)
        self.change_field_contact_value("lastname", contact.lastname)
        self.change_field_contact_value("middlename", contact.middlename)
        self.change_field_contact_value("nickname", contact.nickname)
        self.change_field_contact_value("address", contact.address)
        self.change_field_contact_value("home", contact.homephone)
        self.change_field_contact_value("work", contact.workphone)
        self.change_field_contact_value("mobile", contact.mobilephone)
        self.change_field_contact_value("email", contact.email)
        self.change_field_contact_value("email2", contact.email2)
        self.change_field_contact_value("email3", contact.email3)
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
                element.clear_phone()
                element.send_keys(text)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init modify contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # modify contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        elements = wd.find_elements_by_name("selected[]")
        if index < len(elements):
            elements[index].click()
        else:
            raise IndexError("Index out of range for the contact list.")
        wd.find_elements_by_name("selected[]")[index].click()
        elements[index].click()
        wd.execute_script("window.scrollBy(0, 800);")
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

#    def get_contact_list(self):
#        if self.contact_cache is None:
#            wd = self.app.wd
#            self.open_contact_page()
#            self.contact_cache = []
#            # Поиск всех строк таблицы с контактами
#            rows = wd.find_elements_by_css_selector("tr[name='entry']")
#            for row in rows:
#                cells = row.find_elements_by_tag_name("td")
#                # Получаем ID контакта из чекбокса
#                checkbox = cells[0].find_element_by_tag_name("input")
#                contact_id = checkbox.get_attribute("value")
#                # Имя и фамилия находятся в других ячейках
#                lastname = cells[1].text
#                firstname = cells[2].text
#                # Адрес
#                address = cells[3].text
#                # Вычленяем телефоны
#                all_phones = cells[5].text
#                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, contact_id=contact_id, address=address,
#                                                  all_phones_from_home_page=all_phones))
#        return list(self.contact_cache)


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.NAME, "selected[]")))
            self.contact_cache = []
            rows = wd.find_elements_by_css_selector("tr[name='entry']")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                checkbox = cells[0].find_element_by_tag_name("input")
                contact_id = checkbox.get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,  contact_id=contact_id, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        entries = wd.find_elements_by_name("entry")
        row = entries[index]
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

#    def select_contact_by_index(self, index):
#        wd = self.app.wd
#        self.open_contact_page()
#        wd.find_elements_by_name("selected[]")[index].click()

#    def open_contact_to_edit_by_index(self, index):
#        wd = self.app.wd
#        self.select_contact_by_index(index)
#        rows = wd.find_elements_by_name("entry")
#        if index < len(rows):
#            row = rows[index]
#            edit_button = row.find_element_by_css_selector("a[href*='edit.php?id=']")
#            edit_button.click()

    def open_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

#    def get_contact_info_from_edit_page(self, index):
#        wd = self.app.wd
#        self.open_contact_to_edit_by_index(index)
#        firstname = wd.find_element_by_name('firstname').get_attribute('value')
#        lastname = wd.find_element_by_name('lastname').get_attribute('value')
#        id = wd.find_element_by_name('id').get_attribute('value')
#        homenomber = wd.find_element_by_name('home').get_attribute('value')
#        worknomber = wd.find_element_by_name('work').get_attribute('value')
#        mobilenomber = wd.find_element_by_name('mobile').get_attribute('value')
#        address = wd.find_element_by_name('address').get_attribute('value')
#        email = wd.find_element_by_name('email').get_attribute('value')
#        email2 = wd.find_element_by_name('email2').get_attribute('value')
#        email3 = wd.find_element_by_name('email3').get_attribute('value')
#
#        return Contact(firstname=firstname, lastname=lastname, id=id,
#                       homenomber=homenomber, mobilenomber=mobilenomber,
#                       worknomber=worknomber, address=address, email=email, email2=email2, email3=email3)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, contact_id=contact_id, address=address,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)
