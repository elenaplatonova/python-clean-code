from messy_code import (
    can_cancel,
    can_delete,
    can_edit,
    get_permissions,
    get_status_label,
    is_fulfilled,
)


def test_admin_permissions():
    assert get_permissions({"role": "admin"}) == ["read", "write", "delete", "manage_users"]


def test_editor_permissions():
    assert get_permissions({"role": "editor"}) == ["read", "write"]


def test_viewer_permissions():
    assert get_permissions({"role": "viewer"}) == ["read"]


def test_unknown_role_permissions():
    assert get_permissions({"role": "guest"}) == []


def test_admin_can_delete():
    assert can_delete({"role": "admin"}) is True


def test_editor_cannot_delete():
    assert can_delete({"role": "editor"}) is False


def test_admin_can_edit():
    assert can_edit({"role": "admin"}) is True


def test_editor_can_edit():
    assert can_edit({"role": "editor"}) is True


def test_viewer_cannot_edit():
    assert can_edit({"role": "viewer"}) is False


def test_status_pending():
    assert get_status_label({"status": "pending"}) == "Awaiting payment"


def test_status_processing():
    assert get_status_label({"status": "processing"}) == "Being prepared"


def test_status_shipped():
    assert get_status_label({"status": "shipped"}) == "On the way"


def test_status_delivered():
    assert get_status_label({"status": "delivered"}) == "Delivered"


def test_status_cancelled():
    assert get_status_label({"status": "cancelled"}) == "Cancelled"


def test_status_unknown():
    assert get_status_label({"status": "refunded"}) == "Unknown"


def test_can_cancel_pending():
    assert can_cancel({"status": "pending"}) is True


def test_can_cancel_processing():
    assert can_cancel({"status": "processing"}) is True


def test_cannot_cancel_shipped():
    assert can_cancel({"status": "shipped"}) is False


def test_is_fulfilled_shipped():
    assert is_fulfilled({"status": "shipped"}) is True


def test_is_fulfilled_delivered():
    assert is_fulfilled({"status": "delivered"}) is True


def test_not_fulfilled_pending():
    assert is_fulfilled({"status": "pending"}) is False
