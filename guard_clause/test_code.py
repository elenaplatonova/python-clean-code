from messy_code import process_payment

ACTIVE_USER = {"is_active": True, "credit_limit": 500}
INACTIVE_USER = {"is_active": False, "credit_limit": 500}


def test_successful_payment():
    result = process_payment(ACTIVE_USER, {"total": 100})
    assert result == {"status": "ok", "charge": 108.0}


def test_charge_includes_8_percent_tax():
    result = process_payment(ACTIVE_USER, {"total": 50})
    assert result == {"status": "ok", "charge": 54.0}


def test_no_user_returns_error():
    result = process_payment(None, {"total": 100})
    assert result["status"] == "error"
    assert result["reason"] == "no_user"


def test_inactive_user_returns_error():
    result = process_payment(INACTIVE_USER, {"total": 100})
    assert result["status"] == "error"
    assert result["reason"] == "inactive_user"


def test_no_order_returns_error():
    result = process_payment(ACTIVE_USER, None)
    assert result["status"] == "error"
    assert result["reason"] == "no_order"


def test_zero_total_returns_error():
    result = process_payment(ACTIVE_USER, {"total": 0})
    assert result["status"] == "error"
    assert result["reason"] == "invalid_total"


def test_negative_total_returns_error():
    result = process_payment(ACTIVE_USER, {"total": -10})
    assert result["status"] == "error"
    assert result["reason"] == "invalid_total"


def test_exceeds_credit_limit_returns_error():
    result = process_payment(ACTIVE_USER, {"total": 600})
    assert result["status"] == "error"
    assert result["reason"] == "exceeds_credit"
