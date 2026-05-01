def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return "User not found"


def calculate_discount(order_total, coupon_code):
    if order_total <= 0:
        return "Error: invalid total"
    if coupon_code == "SAVE10":
        return order_total * 0.10
    if coupon_code == "SAVE20":
        return order_total * 0.20
    return False


def get_page_count(total_items, page_size):
    if page_size == 0:
        return None
    if total_items == 0:
        return "no items"
    return -(-total_items // page_size)
