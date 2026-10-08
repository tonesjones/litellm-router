from shop.pricing import apply_discount


def test_uppercase_code():
    assert apply_discount(100, "SAVE10") == 90


def test_lowercase_code():
    assert apply_discount(100, "save10") == 90


def test_mixed_case_code():
    assert apply_discount(100, "Save25") == 75
