# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(group_name="Random123", group_header="Random123", group_footer="Random123"))


def test_add_empty_group(app):
    app.group.create(Group(group_name="", group_header="", group_footer=""))
