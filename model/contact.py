from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, middlename=None, nickname=None, address=None,
                 all_phones_from_home_page=None, homephone=None, mobilephone=None, workphone=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None,
                 bday=None, bmonth=None, byear=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
