from messy_code import get_user_msg_from_error_log, summarize_scores


def test_extract_full_output():
    result = get_user_msg_from_error_log("2024-01-15T09:32:11 ERROR failed to connect")
    assert result == "Hi, we have 1 error(s) at 2024-01-15 09:32:11: failed to connect"


def test_extract_date():
    result = get_user_msg_from_error_log("2024-01-15T09:32:11 ERROR failed to connect")
    assert "2024-01-15" in result


def test_extract_time():
    result = get_user_msg_from_error_log("2024-01-15T09:32:11 ERROR failed to connect")
    assert "09:32:11" in result


def test_extract_level_lowercased():
    result = get_user_msg_from_error_log("2024-01-15T09:32:11 ERROR failed to connect")
    assert "error" in result


def test_extract_message():
    result = get_user_msg_from_error_log("2024-01-15T09:32:11 ERROR failed to connect")
    assert "failed to connect" in result


def test_extract_message_strips_whitespace():
    result = get_user_msg_from_error_log("2024-01-15T09:32:11 INFO   user logged in  ")
    assert result.endswith("user logged in")


def test_extract_info_level():
    result = get_user_msg_from_error_log("2024-03-22T14:00:00 INFO server started")
    assert "info" in result


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
