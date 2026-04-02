import string
import pytest

from passgen import create_alphabet, generate_password, generate_passwords

def test_password_length():
    alphabet = create_alphabet(False, False)
    password = generate_password(16, alphabet)

    assert len(password) == 16

def test_password_count():
    alphabet = create_alphabet(False, False)
    passwords = generate_passwords(12, 3, alphabet)

    assert len(passwords) == 3
    
def test_no_digits():
    alphabet = create_alphabet(False, True)
    passwords = generate_passwords(20, 5, alphabet)

    for p in passwords:
        assert not any(c.isdigit() for c in p)

def test_no_symbols():
    alphabet = create_alphabet(True, False)
    passwords = generate_passwords(20, 5, alphabet)
    
    for p in passwords:
        assert not any(c in string.punctuation for c in p)

def test_invalid_length():
    alphabet = create_alphabet(False, False)

    with pytest.raises(ValueError):
        generate_password(0, alphabet)

def test_invalid_count():
    alphabet = create_alphabet(False, False)

    with pytest.raises(ValueError):
        generate_passwords(10, 0, alphabet)

def test_empty_alphabet():
    with pytest.raises(ValueError):
        generate_password(10, "")