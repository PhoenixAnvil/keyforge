# tests/test_forge.py

from keyforge import forge


def test_rand_between_inclusive():
    for _ in range(100):
        r = forge.rand_between(5, 10)
        assert 5 <= r <= 10


def test_random_letter_output():
    for _ in range(100):
        c = forge.random_letter()
        assert c.isalpha()
        assert len(c) == 1


def test_random_digit_output():
    for _ in range(100):
        c = forge.random_digit()
        assert c.isdigit()
        assert len(c) == 1


def test_random_special_output():
    for _ in range(100):
        c = forge.random_special()
        assert not c.isalnum()
        assert len(c) == 1


def test_forge_password_combo():
    pwd = forge.forge_password(
        length=12, alpha=False, numeric=False, special=False, combo=True
    )
    assert len(pwd) == 12
    assert any(c.isalpha() for c in pwd)
    assert any(c.isdigit() for c in pwd)
    assert any(not c.isalnum() for c in pwd)


def test_forge_password_alpha_only():
    pwd = forge.forge_password(
        length=8, alpha=True, numeric=False, special=False, combo=False
    )
    assert len(pwd) == 8
    assert all(c.isalpha() for c in pwd)


def test_forge_password_numeric_only():
    pwd = forge.forge_password(
        length=6, alpha=False, numeric=True, special=False, combo=False
    )
    assert len(pwd) == 6
    assert all(c.isdigit() for c in pwd)


def test_forge_password_special_only():
    pwd = forge.forge_password(
        length=10, alpha=False, numeric=False, special=True, combo=False
    )
    assert len(pwd) == 10
    assert all(not c.isalnum() for c in pwd)
