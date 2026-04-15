from messy_code import load_json, parse_int, parse_price


def test_parse_int_valid():
    assert parse_int("42") == 42


def test_parse_int_negative():
    assert parse_int("-10") == -10


def test_parse_int_invalid_string():
    assert parse_int("abc") == 0


def test_parse_int_float_string():
    assert parse_int("3.14") == 0


def test_parse_price_simple():
    assert parse_price("9.99") == 9.99


def test_parse_price_with_dollar():
    assert parse_price("$19.99") == 19.99


def test_parse_price_with_comma():
    assert parse_price("1,299.00") == 1299.0


def test_parse_price_invalid():
    assert parse_price("free") is None


def test_load_json_valid(tmp_path):
    p = tmp_path / "config.json"
    p.write_text('{"key": "value"}')
    assert load_json(str(p)) == {"key": "value"}


def test_load_json_missing_file():
    assert load_json("/nonexistent/path.json") == {}


def test_load_json_invalid_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("not json")
    assert load_json(str(p)) == {}
