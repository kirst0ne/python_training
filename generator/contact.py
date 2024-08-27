from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            bday=random_day(), bmonth=random_month(), byear=random_year())
            for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
