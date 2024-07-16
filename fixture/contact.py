

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init create contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def fill_contact_form(self, contact):
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("bday", contact.bday)
        self.change_field_value_contact("bmonth", contact.bmonth)
        self.change_field_value_contact("byear", contact.byear)

    def change_field_value_contact(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            element = wd.find_element_by_name(field_name).click()
            element.clear()
            element.send_keys(value)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # init modify contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # modify contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.execute_script("window.scrollBy(0, 800);")
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
