from model.group import Group
import random
import string


constant = [
    Group(group_name="name1", group_header="header1", group_footer="footer1"),
    Group(group_name="name2", group_header="header2", group_footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*6
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("group_name", 10), group_header=random_string("group_header", 20),
          group_footer=random_string("group_footer", 20))
    for i in range(5)
]
