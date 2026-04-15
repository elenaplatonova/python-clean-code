import logging

from messy_code import parse_config, process_record, read_user_file

# --- parse_config ---

def test_parse_config_valid():
    assert parse_config('{"key": "value"}') == {"key": "value"}


def test_parse_config_invalid_returns_empty():
    assert parse_config("not json") == {}


def test_parse_config_logs_on_invalid(caplog):
    with caplog.at_level(logging.ERROR):
        parse_config("not valid json")
    assert len(caplog.records) > 0


def test_parse_config_log_contains_useful_info(caplog):
    with caplog.at_level(logging.ERROR):
        parse_config("bad input")
    assert any("parse_config" in r.message or "bad input" in r.message for r in caplog.records)


# --- process_record ---

def test_process_record_valid():
    record = {"id": "1", "value": "42", "score": "9.5"}
    assert process_record(record) == {"id": "1", "value": 42, "score": 9.5}


def test_process_record_missing_key_returns_none():
    assert process_record({"id": "1"}) is None


def test_process_record_invalid_value_returns_none():
    assert process_record({"id": "1", "value": "bad", "score": "9.5"}) is None


def test_process_record_logs_on_missing_key(caplog):
    with caplog.at_level(logging.ERROR):
        process_record({"id": "1"})
    assert len(caplog.records) > 0


def test_process_record_logs_on_invalid_value(caplog):
    with caplog.at_level(logging.ERROR):
        process_record({"id": "1", "value": "bad", "score": "9.5"})
    assert len(caplog.records) > 0


# --- read_user_file ---

def test_read_user_file_valid(tmp_path):
    p = tmp_path / "users.json"
    p.write_text('[{"id": 1, "name": "Alice"}]')
    assert read_user_file(str(p)) == [{"id": 1, "name": "Alice"}]


def test_read_user_file_missing_returns_empty():
    assert read_user_file("/nonexistent/file.json") == []


def test_read_user_file_logs_on_missing(caplog):
    with caplog.at_level(logging.ERROR):
        read_user_file("/nonexistent/file.json")
    assert len(caplog.records) > 0


def test_read_user_file_invalid_json_returns_empty(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("not json")
    assert read_user_file(str(p)) == []


def test_read_user_file_logs_on_invalid_json(caplog, tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("not json")
    with caplog.at_level(logging.ERROR):
        read_user_file(str(p))
    assert len(caplog.records) > 0
