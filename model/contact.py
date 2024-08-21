from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, middlename=None, nickname=None, address=None, mobile=None, email=None, bday=None, bmonth=None, byear=None, contact_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.address = address
        self.mobile = mobile
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
