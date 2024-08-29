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
        self.open_creating_contact()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_creating_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        self.filling_contact_write("firstname", contact.firstname)
        self.filling_contact_write("lastname", contact.lastname)
        self.filling_contact_write("middlename", contact.middlename)
        self.filling_contact_write("nickname", contact.nickname)
        self.filling_contact_write("address", contact.address)
        self.filling_contact_write("home", contact.homephone)
        self.filling_contact_write("work", contact.workphone)
        self.filling_contact_write("mobile", contact.mobilephone)
        self.filling_contact_write("email", contact.email)
        self.filling_contact_write("email2", contact.email2)
        self.filling_contact_write("email3", contact.email3)
        self.change_contact_choose("bday", contact.bday)
        self.change_contact_choose("bmonth", contact.bmonth)
        self.filling_contact_write("byear", contact.byear)

    def change_contact_choose(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_contact_value(self, field_name, text):
        wd = self.app.wd
        element = wd.find_element_by_name(field_name)
        if element.tag_name.lower() == "select":
            Select(element).select_by_visible_text(text)
        else:
            element.clear()
            element.send_keys(text)

    def filling_contact_write(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()

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

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_edit_page_by_id(id)
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_contact_page()
        self.contact_cache = None

    def open_edit_page_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        edit_button = wd.find_element_by_css_selector(f"a[href*='edit.php?id={id}']")
        edit_button.click()

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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

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
                id = checkbox.get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,  id=id, address=address,
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

    def open_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
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
