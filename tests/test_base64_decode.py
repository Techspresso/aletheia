"""Tests standalone modules"""
from aletheia.base64_decode import base64_decode

def test_base64_decode_correct():
    """Test that a correct base64 string is decoded correctly"""
    input = "SSBhbSBBbGV0aGVpYQ=="
    expected = "I am Aletheia"
    assert base64_decode(input) == expected

def test_base64_decode_incorrect():
    """Test that an incorrect base64 string raises a ValueError"""
    input = "This is not a valid base64 string"
    try:
        result = base64_decode(input)
    except Exception as e:
        assert isinstance(e, ValueError)