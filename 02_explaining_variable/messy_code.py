import re


def extract_report_data(log_line):
    parts = re.match(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)", log_line)
    return {"date": parts.group(1), "time": parts.group(2), "level": parts.group(3), "message": parts.group(4).strip()}


def summarize_scores(scores):
    return {"top_3_avg": round(sum(scores[: len(scores) // 3 if len(scores) % 3 == 0 else len(scores) // 3 + 1]) / (len(scores) // 3 if len(scores) % 3 == 0 else len(scores) // 3 + 1), 2), "bottom_half": scores[(len(scores) + 1) // 2 :]}
