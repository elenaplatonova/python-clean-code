import json


def parse_int(value):
    try:
        return int(value)
    except:
        return 0


def parse_price(text):
    try:
        return round(float(text.strip().replace(",", "").replace("$", "")), 2)
    except Exception as e:
        return None


def load_json(filepath):
    try:
        with open(filepath) as f:
            return json.load(f)
    except:
        return {}
