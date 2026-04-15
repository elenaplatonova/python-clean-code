from messy_code import get_config_value, get_first_tag, get_nested_value, has_permission

# --- get_config_value ---

def test_get_config_value_existing_key():
    assert get_config_value({"host": "localhost", "port": 5432}, "host") == "localhost"


def test_get_config_value_missing_key_returns_none():
    assert get_config_value({"host": "localhost"}, "port") is None


def test_get_config_value_custom_default():
    assert get_config_value({}, "timeout", 30) == 30


# --- has_permission ---

def test_has_permission_true():
    user = {"permissions": ["read", "write"]}
    assert has_permission(user, "read") is True


def test_has_permission_false():
    user = {"permissions": ["read"]}
    assert has_permission(user, "write") is False


def test_has_permission_no_permissions_key():
    assert has_permission({}, "read") is False


# --- get_first_tag ---

def test_get_first_tag_exists():
    assert get_first_tag({"tags": ["python", "clean"]}) == "python"


def test_get_first_tag_empty_list():
    assert get_first_tag({"tags": []}) is None


def test_get_first_tag_no_tags_key():
    assert get_first_tag({}) is None


# --- get_nested_value ---

def test_get_nested_value_exists():
    data = {"user": {"name": "Alice"}}
    assert get_nested_value(data, "user", "name") == "Alice"


def test_get_nested_value_missing_outer_key():
    assert get_nested_value({}, "user", "name") is None


def test_get_nested_value_missing_inner_key():
    data = {"user": {"email": "a@b.com"}}
    assert get_nested_value(data, "user", "name") is None


def test_get_nested_value_custom_default():
    assert get_nested_value({}, "user", "name", default="anonymous") == "anonymous"


def test_get_nested_value_outer_not_a_dict():
    data = {"user": "not_a_dict"}
    assert get_nested_value(data, "user", "name") is None
