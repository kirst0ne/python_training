import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, group_name, group_header, group_footer) = row
                list.append(Group(group_id=str(group_id), group_name=group_name, group_header=group_header,
                                  group_footer=group_footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook WHERE deprecated IS NULL")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                  homephone=home, mobilephone=mobile, workphone=work,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()


def clean(data):
    parts = data.split(':')
    cleaned_parts = [part.strip() for part in parts]
    cleaned_string = ':'.join(cleaned_parts)
    cleaned_string = re.sub(r'\s{2,}', ' ', cleaned_string)
    return cleaned_string
