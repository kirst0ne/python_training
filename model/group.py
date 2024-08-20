from sys import maxsize


class Group:

    def __init__(self, group_name=None, group_header=None, group_footer=None, group_id=None):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s" % (self.group_id, self.group_name)

    def __eq__(self, other):
        return (self.group_id is None or other.group_id is None or self.group_id == other.group_id) and self.group_name == other.group_name

    def id_or_max(self):
        if self.group_id:
            return int(self.group_id)
        else:
            return maxsize
