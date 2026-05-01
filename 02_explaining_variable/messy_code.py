def extract_report_data(log_line):
    return {"date": log_line.split("T")[0], "time": log_line.split()[0].split("T")[1], "level": log_line.split()[1], "message": " ".join(log_line.split()[2:])}


def summarize_scores(scores):
    return {"top_3_avg": round(sum(scores[: len(scores) // 3 if len(scores) % 3 == 0 else len(scores) // 3 + 1]) / (len(scores) // 3 if len(scores) % 3 == 0 else len(scores) // 3 + 1), 2), "bottom_half": scores[(len(scores) + 1) // 2 :]}
