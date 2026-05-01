import re


def get_user_msg_from_error_log(log_line):
    """Parse a raw log line and return a human-readable message.

    Input:  "2024-01-15T09:32:11 ERROR failed to connect"
    Output: "Hi, we have 1 error(s) at 2024-01-15 09:32:11: failed to connect"
    """
    parts = re.match(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)", log_line)
    return f"Hi, we have 1 {parts.group(3).lower()}(s) at {parts.group(1)} {parts.group(2)}: {parts.group(4).strip()}"


def summarize_scores(scores):
    """Summarize a pre-sorted (descending) list of scores.

    top_third_avg: average of the top one-third of scores (ceiling division,
                   so 10 scores → first 4; 9 scores → first 3).
    bottom_half:   the lower half of the list (everything from the midpoint on).
    """
    return {"top_third_avg": round(sum(scores[: len(scores) // 3 if len(scores) % 3 == 0 else len(scores) // 3 + 1]) / (len(scores) // 3 if len(scores) % 3 == 0 else len(scores) // 3 + 1), 2), "bottom_half": scores[(len(scores) + 1) // 2 :]}
