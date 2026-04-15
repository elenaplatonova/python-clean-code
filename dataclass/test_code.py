from messy_code import (
    create_user,
    get_display_name,
    is_eligible_for_admin,
    promote_user,
    transfer_role,
)


def test_create_user_defaults_to_viewer():
    user = create_user("Alice", "alice@example.com", 30)
    assert user.role == "viewer"


def test_create_user_custom_role():
    user = create_user("Bob", "bob@example.com", 25, role="editor")
    assert user.role == "editor"


def test_create_user_stores_name_and_email():
    user = create_user("Alice", "alice@example.com", 30)
    assert user.name == "Alice"
    assert user.email == "alice@example.com"


def test_create_user_stores_age():
    user = create_user("Alice", "alice@example.com", 30)
    assert user.age == 30


def test_promote_viewer_becomes_editor():
    user = create_user("Alice", "alice@example.com", 30)
    promoted = promote_user(user)
    assert promoted.role == "editor"


def test_promote_editor_becomes_admin():
    user = create_user("Alice", "alice@example.com", 30, role="editor")
    promoted = promote_user(user)
    assert promoted.role == "admin"


def test_promote_admin_stays_admin():
    user = create_user("Alice", "alice@example.com", 30, role="admin")
    promoted = promote_user(user)
    assert promoted.role == "admin"


def test_get_display_name_format():
    user = create_user("Alice", "alice@example.com", 30)
    assert get_display_name(user) == "Alice <alice@example.com>"


def test_is_eligible_for_admin_true():
    user = create_user("Alice", "alice@example.com", 25, role="editor")
    assert is_eligible_for_admin(user) is True


def test_is_eligible_for_admin_too_young():
    user = create_user("Bob", "bob@example.com", 16, role="editor")
    assert is_eligible_for_admin(user) is False


def test_is_eligible_for_admin_wrong_role():
    user = create_user("Carol", "carol@example.com", 30, role="viewer")
    assert is_eligible_for_admin(user) is False


def test_transfer_role():
    source = create_user("Alice", "alice@example.com", 30, role="admin")
    target = create_user("Bob", "bob@example.com", 25, role="viewer")
    updated_source, updated_target = transfer_role(source, target)
    assert updated_source.role == "viewer"
    assert updated_target.role == "admin"
