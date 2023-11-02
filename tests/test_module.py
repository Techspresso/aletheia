"""Tests standalone modules"""
import module

def test_amodule():
    """Test amodule.hello()."""
    assert module.yo() == 'Yo module!', 'module.yo() returns "Yo module!"'
