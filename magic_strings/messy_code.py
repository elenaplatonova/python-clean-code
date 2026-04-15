def get_permissions(user):
    if user["role"] == "admin":
        return ["read", "write", "delete", "manage_users"]
    elif user["role"] == "editor":
        return ["read", "write"]
    elif user["role"] == "viewer":
        return ["read"]
    return []


def can_delete(user):
    return user["role"] == "admin"


def can_edit(user):
    return user["role"] in ["admin", "editor"]


def get_status_label(order):
    if order["status"] == "pending":
        return "Awaiting payment"
    elif order["status"] == "processing":
        return "Being prepared"
    elif order["status"] == "shipped":
        return "On the way"
    elif order["status"] == "delivered":
        return "Delivered"
    elif order["status"] == "cancelled":
        return "Cancelled"
    return "Unknown"


def can_cancel(order):
    return order["status"] in ["pending", "processing"]


def is_fulfilled(order):
    return order["status"] in ["shipped", "delivered"]
