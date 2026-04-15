class User:
    def __init__(self, name, email, age, role="viewer"):
        self.name = name
        self.email = email
        self.age = age
        self.role = role


def create_user(name, email, age, role="viewer"):
    u = User.__new__(User)
    u.name = name
    u.email = email
    u.age = age
    u.role = role
    return u


def promote_user(user):
    if user.role == "viewer":
        user.role = "editor"
    elif user.role == "editor":
        user.role = "admin"
    return user


def get_display_name(user):
    return user.name + " <" + user.email + ">"


def is_eligible_for_admin(user):
    if user.age >= 18:
        if user.role == "editor":
            return True
    return False


def transfer_role(source, target):
    tmp = source.role
    source.role = "viewer"
    target.role = tmp
    return source, target
