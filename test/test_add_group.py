# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*6
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("group_name", 10), group_header=random_string("group_header", 20),
          group_footer=random_string("group_footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
