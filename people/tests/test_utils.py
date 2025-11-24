import pytest
from people.utils import is_valid_cpf, only_digits

def test_only_digits_removes_non_numeric():
    assert only_digits("123.456-789") == "123456789"
    assert only_digits("abc123") == "123"
    assert only_digits("") == ""

def test_is_valid_cpf_valid_examples():
    assert is_valid_cpf("52998224725") is True

def test_is_valid_cpf_invalid_examples():
    assert is_valid_cpf("11111111111") is False
    assert is_valid_cpf("12345678900") is False
    assert is_valid_cpf("12345") is False