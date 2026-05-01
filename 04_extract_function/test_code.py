import messy_code

SCORES = [85, 92, 78, 96, 71, 88, 63, 79, 91, 84]
WEIGHTS = [1, 2, 1, 2, 1, 1, 1, 1, 2, 1]
THRESHOLDS = {"A": 85, "B": 75, "C": 65, "pass": 70}


def test_generate_report_returns_all_keys():
    result = messy_code.generate_report(SCORES, WEIGHTS, THRESHOLDS)
    assert set(result.keys()) == {"weighted_average", "top_scorers", "pass_rate", "grade"}


def test_generate_report_weighted_average():
    result = messy_code.generate_report(SCORES, WEIGHTS, THRESHOLDS)
    assert result["weighted_average"] == 85.08


def test_generate_report_top_scorers():
    result = messy_code.generate_report(SCORES, WEIGHTS, THRESHOLDS)
    assert result["top_scorers"] == [96]


def test_generate_report_pass_rate():
    result = messy_code.generate_report(SCORES, WEIGHTS, THRESHOLDS)
    assert result["pass_rate"] == 90.0


def test_generate_report_grade_a():
    result = messy_code.generate_report(SCORES, WEIGHTS, THRESHOLDS)
    assert result["grade"] == "A"


def test_generate_report_grade_b():
    scores = [75, 82, 78, 80, 77, 83, 79, 81]
    result = messy_code.generate_report(scores, [1] * 8, THRESHOLDS)
    assert result["grade"] == "B"


def test_generate_report_grade_c():
    scores = [65, 70, 68, 72, 66, 71, 69, 67]
    result = messy_code.generate_report(scores, [1] * 8, THRESHOLDS)
    assert result["grade"] == "C"


def test_generate_report_grade_f():
    scores = [40, 50, 45, 48, 52, 44, 46, 49]
    result = messy_code.generate_report(scores, [1] * 8, THRESHOLDS)
    assert result["grade"] == "F"


def test_generate_report_no_top_scorers():
    scores = [60, 65, 70, 75, 80]
    result = messy_code.generate_report(scores, [1] * 5, THRESHOLDS)
    assert result["top_scorers"] == []


# --- The four tests below start RED. They define the constraint. ---
# Your job: extract each calculation into its own named function.


def test_weighted_average():
    fn = getattr(messy_code, "weighted_average", None)
    assert fn is not None, "Extract weighted average into a function called 'weighted_average'"
    assert fn([80, 90, 100], [1, 2, 1]) == 90.0


def test_top_scorers():
    fn = getattr(messy_code, "top_scorers", None)
    assert fn is not None, "Extract top scorers logic into a function called 'top_scorers'"
    assert fn([70, 85, 60, 95, 78, 88, 91, 72, 66, 83]) == [95]


def test_pass_rate():
    fn = getattr(messy_code, "pass_rate", None)
    assert fn is not None, "Extract pass rate calculation into a function called 'pass_rate'"
    assert fn([80, 60, 90, 70, 50], 70) == 60.0


def test_letter_grade():
    fn = getattr(messy_code, "letter_grade", None)
    assert fn is not None, "Extract grade assignment into a function called 'letter_grade'"
    t = {"A": 90, "B": 80, "C": 70, "pass": 60}
    assert fn(92, t) == "A"
    assert fn(85, t) == "B"
    assert fn(75, t) == "C"
    assert fn(55, t) == "F"
