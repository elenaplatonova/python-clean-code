import pytest
from messy_code import calculate_discount, find_user, get_page_count

USERS = [
    {"id": "1", "name": "Alice"},
    {"id": "2", "name": "Bob"},
]


# --- find_user ---

def test_find_user_found():
    result = find_user(USERS, "1")
    assert result["name"] == "Alice"


def test_find_user_found_second():
    result = find_user(USERS, "2")
    assert result["name"] == "Bob"


def test_find_user_not_found_returns_none():
    result = find_user(USERS, "999")
    assert result is None


def test_find_user_empty_list_returns_none():
    assert find_user([], "1") is None


# --- calculate_discount ---

def test_discount_save10():
    assert calculate_discount(100, "SAVE10") == 10.0


def test_discount_save20():
    assert calculate_discount(100, "SAVE20") == 20.0


def test_discount_no_coupon_returns_zero():
    assert calculate_discount(100, "INVALID") == 0.0


def test_discount_invalid_total_raises():
    with pytest.raises(ValueError):
        calculate_discount(-10, "SAVE10")


def test_discount_zero_total_raises():
    with pytest.raises(ValueError):
        calculate_discount(0, "SAVE10")


# --- get_page_count ---

def test_page_count_exact():
    assert get_page_count(100, 10) == 10


def test_page_count_partial_page():
    assert get_page_count(101, 10) == 11


def test_page_count_zero_items_returns_zero():
    assert get_page_count(0, 10) == 0


def test_page_count_zero_page_size_raises():
    with pytest.raises(ValueError):
        get_page_count(100, 0)


def test_page_count_one_item():
    assert get_page_count(1, 10) == 1
