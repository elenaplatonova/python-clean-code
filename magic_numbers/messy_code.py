def calculate_order_total(subtotal, user_age):
    if subtotal > 1000:
        discount = subtotal * 0.15
    elif subtotal > 500:
        discount = subtotal * 0.08
    else:
        discount = 0

    if user_age >= 65:
        discount += subtotal * 0.10

    total = subtotal - discount
    tax = total * 0.20
    return round(total + tax, 2)


def is_eligible_for_credit(user):
    return (
        user["age"] >= 18
        and user["credit_score"] >= 650
        and user["annual_income"] >= 25000
    )


def paginate(items, page):
    start = (page - 1) * 25
    end = start + 25
    return items[start:end]


def apply_late_fee(account):
    if account["days_overdue"] > 30:
        fee = account["balance"] * 0.05
    elif account["days_overdue"] > 7:
        fee = account["balance"] * 0.02
    else:
        fee = 0
    return round(fee, 2)
