def generate_report(scores, weights, thresholds):
    weighted_avg = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
    cutoff = sorted(scores)[int(len(scores) * 0.8)]
    top = [s for s in scores if s > cutoff]
    passing = round(len([s for s in scores if s >= thresholds["pass"]]) / len(scores) * 100, 1)
    grade = "A" if weighted_avg >= thresholds["A"] else "B" if weighted_avg >= thresholds["B"] else "C" if weighted_avg >= thresholds["C"] else "F"
    return {"weighted_average": round(weighted_avg, 2), "top_scorers": top, "pass_rate": passing, "grade": grade}
