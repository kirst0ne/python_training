from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*6
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_phone_number():
    digits = string.digits
    return "+7" + "".join([random.choice(digits) for _ in range(10)])


def random_month():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return random.choice(months)


def random_day():
    return str(random.randint(1, 31))


def random_year():
    return str(random.randint(1917, 2024))


def random_email(prefix, maxlen):
    domains = ["gmail.com", "outlook.com", "bk.com", "mail.ru", "yandex.ru"]
    return (prefix + "".join([random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, maxlen))])
            + "@" + random.choice(domains))


testdata = [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            middlename=random_string("middlename", 20), nickname=random_string("nickname", 10),
            address=random_string("address", 50),
            homephone=random_phone_number(), workphone=random_phone_number(), mobilephone=random_phone_number(),
            email=random_email("email", 10), email2=random_email("email", 10), email3=random_email("email", 10),
            bday=random_day(), bmonth=random_month(), byear=random_year())]
