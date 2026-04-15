from messy_code import get_discounted_prices, get_expensive_names, get_product_names

PRODUCTS = [
    {"name": "  apple ", "price": 1.20, "in_stock": True},
    {"name": "banana", "price": 0.50, "in_stock": False},
    {"name": " cherry", "price": 3.00, "in_stock": True},
    {"name": "date  ", "price": 5.00, "in_stock": True},
]


def test_discounted_prices_skips_out_of_stock():
    result = get_discounted_prices(PRODUCTS)
    assert result == [1.08, 2.70, 4.50]


def test_discounted_prices_empty_list():
    assert get_discounted_prices([]) == []


def test_discounted_prices_all_out_of_stock():
    products = [{"name": "x", "price": 10.0, "in_stock": False}]
    assert get_discounted_prices(products) == []


def test_get_product_names_strips_and_titles():
    result = get_product_names(PRODUCTS)
    assert result == ["Apple", "Banana", "Cherry", "Date"]


def test_get_product_names_empty():
    assert get_product_names([]) == []


def test_get_expensive_names_filters_correctly():
    result = get_expensive_names(PRODUCTS, threshold=1.00)
    assert result == ["  apple ", " cherry", "date  "]


def test_get_expensive_names_nothing_above_threshold():
    result = get_expensive_names(PRODUCTS, threshold=100)
    assert result == []
