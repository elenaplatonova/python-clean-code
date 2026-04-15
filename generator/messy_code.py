def parse_log_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    records = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 3:
            continue
        records.append({"timestamp": parts[0].strip(), "level": parts[1].strip(), "message": parts[2].strip()})

    return records


def count_errors(filepath):
    records = parse_log_file(filepath)
    return sum(1 for r in records if r["level"] == "ERROR")


def first_critical(filepath):
    records = parse_log_file(filepath)
    for record in records:
        if record["level"] == "CRITICAL":
            return record
    return None
