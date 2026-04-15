
import pytest
from messy_code import count_errors, first_critical, parse_log_file

LOG_CONTENT = """\
2024-01-01 00:01 | INFO    | server started
2024-01-01 00:02 | ERROR   | disk full
2024-01-01 00:03 | INFO    | cleanup triggered
2024-01-01 00:04 | ERROR   | write failed
2024-01-01 00:05 | CRITICAL| filesystem corrupted
2024-01-01 00:06 | INFO    | shutting down

bad line with no pipes
only two fields here
"""


@pytest.fixture
def log_file(tmp_path):
    p = tmp_path / "test.log"
    p.write_text(LOG_CONTENT)
    return str(p)


def test_parse_returns_correct_count(log_file):
    records = list(parse_log_file(log_file))
    assert len(records) == 6


def test_parse_skips_blank_lines(log_file):
    records = list(parse_log_file(log_file))
    assert all(r["timestamp"] != "" for r in records)


def test_parse_skips_malformed_lines(log_file):
    records = list(parse_log_file(log_file))
    messages = [r["message"] for r in records]
    assert "bad line with no pipes" not in messages


def test_parse_first_record(log_file):
    records = list(parse_log_file(log_file))
    assert records[0] == {
        "timestamp": "2024-01-01 00:01",
        "level": "INFO",
        "message": "server started",
    }


def test_parse_strips_whitespace(log_file):
    records = list(parse_log_file(log_file))
    levels = {r["level"] for r in records}
    assert levels == {"INFO", "ERROR", "CRITICAL"}


def test_count_errors(log_file):
    assert count_errors(log_file) == 2


def test_count_errors_empty_file(tmp_path):
    p = tmp_path / "empty.log"
    p.write_text("")
    assert count_errors(str(p)) == 0


def test_first_critical_found(log_file):
    result = first_critical(log_file)
    assert result is not None
    assert result["level"] == "CRITICAL"
    assert result["message"] == "filesystem corrupted"


def test_first_critical_not_found(tmp_path):
    p = tmp_path / "no_critical.log"
    p.write_text("2024-01-01 | INFO | all good\n")
    assert first_critical(str(p)) is None


def test_parse_log_file_returns_generator(log_file):
    import types
    result = parse_log_file(log_file)
    assert isinstance(result, types.GeneratorType), (
        "parse_log_file must return a generator (use yield, not return list)"
    )
