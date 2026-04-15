from messy_code import extract_report_data, summarize_scores


def test_extract_date():
    result = extract_report_data("2024-01-15T09:32:11 ERROR failed to connect")
    assert result["date"] == "2024-01-15"


def test_extract_time():
    result = extract_report_data("2024-01-15T09:32:11 ERROR failed to connect")
    assert result["time"] == "09:32:11"


def test_extract_level():
    result = extract_report_data("2024-01-15T09:32:11 ERROR failed to connect")
    assert result["level"] == "ERROR"


def test_extract_message():
    result = extract_report_data("2024-01-15T09:32:11 ERROR failed to connect")
    assert result["message"] == "failed to connect"


def test_extract_message_strips_whitespace():
    result = extract_report_data("2024-01-15T09:32:11 INFO   user logged in  ")
    assert result["message"] == "user logged in"


def test_extract_info_level():
    result = extract_report_data("2024-03-22T14:00:00 INFO server started")
    assert result["level"] == "INFO"


def test_summarize_scores_top_avg_divisible():
    # 9 scores: top third = first 3
    result = summarize_scores([90, 85, 80, 70, 60, 50, 40, 30, 20])
    assert result["top_3_avg"] == 85.0


def test_summarize_scores_bottom_half():
    result = summarize_scores([90, 85, 80, 70, 60, 50, 40, 30, 20])
    assert result["bottom_half"] == [50, 40, 30, 20]


def test_summarize_scores_non_divisible():
    # 10 scores: top third rounded up = first 4
    result = summarize_scores([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
    assert result["top_3_avg"] == 85.0


def test_summarize_scores_bottom_half_non_divisible():
    result = summarize_scores([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
    assert result["bottom_half"] == [50, 40, 30, 20, 10]
