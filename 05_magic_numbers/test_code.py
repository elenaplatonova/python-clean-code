from messy_code import (
    apply_late_fee,
    calculate_order_total,
    is_eligible_for_credit,
    paginate,
)


def test_order_large_discount():
    assert calculate_order_total(1200, 30) == round(1200 * 0.85 * 1.20, 2)


def test_order_medium_discount():
    assert calculate_order_total(600, 30) == round(600 * 0.92 * 1.20, 2)


def test_order_no_discount():
    assert calculate_order_total(100, 30) == round(100 * 1.20, 2)


def test_order_senior_discount():
    assert calculate_order_total(100, 65) == round(100 * 0.90 * 1.20, 2)


def test_order_senior_plus_large_discount():
    result = calculate_order_total(1200, 65)
    expected = round(1200 * (1 - 0.15 - 0.10) * 1.20, 2)
    assert result == expected


def test_credit_eligible():
    user = {"age": 25, "credit_score": 700, "annual_income": 30000}
    assert is_eligible_for_credit(user) is True


def test_credit_too_young():
    user = {"age": 17, "credit_score": 700, "annual_income": 30000}
    assert is_eligible_for_credit(user) is False


def test_credit_low_score():
    user = {"age": 25, "credit_score": 600, "annual_income": 30000}
    assert is_eligible_for_credit(user) is False


def test_credit_low_income():
    user = {"age": 25, "credit_score": 700, "annual_income": 20000}
    assert is_eligible_for_credit(user) is False


def test_paginate_first_page():
    items = list(range(100))
    assert paginate(items, 1) == list(range(25))


def test_paginate_second_page():
    items = list(range(100))
    assert paginate(items, 2) == list(range(25, 50))


def test_paginate_partial_last_page():
    items = list(range(30))
    assert paginate(items, 2) == [25, 26, 27, 28, 29]


def test_late_fee_severe():
    account = {"balance": 1000, "days_overdue": 31}
    assert apply_late_fee(account) == 50.0


def test_late_fee_moderate():
    account = {"balance": 1000, "days_overdue": 10}
    assert apply_late_fee(account) == 20.0


def test_late_fee_none():
    account = {"balance": 1000, "days_overdue": 3}
    assert apply_late_fee(account) == 0
