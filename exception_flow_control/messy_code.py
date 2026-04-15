def get_config_value(config, key, default=None):
    try:
        return config[key]
    except KeyError:
        return default


def has_permission(user, permission):
    try:
        return permission in user["permissions"]
    except KeyError:
        return False


def get_first_tag(item):
    try:
        return item["tags"][0]
    except (KeyError, IndexError):
        return None


def get_nested_value(data, key1, key2, default=None):
    try:
        return data[key1][key2]
    except (KeyError, TypeError):
        return default
