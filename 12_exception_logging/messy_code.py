import json


def parse_config(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def process_record(record):
    try:
        return {
            "id": record["id"],
            "value": int(record["value"]),
            "score": float(record["score"]),
        }
    except (KeyError, ValueError):
        return None


def read_user_file(filepath):
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
