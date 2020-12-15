class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # if user in group.users:
    #     return True
    # else:
    #     if len(group.groups) is 0:
    #         return False
    #     else:
    #         for inner_group in group.groups:
    #             return is_user_in_group(user, inner_group)

    # return False
    return user in group.users or any(is_user_in_group(user, sub_group) for sub_group in group.get_groups())


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
no_sub_child_user = "no_sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))
# True

print(is_user_in_group(no_sub_child_user, parent))
# False

print(is_user_in_group(sub_child_user, sub_child))
# True
