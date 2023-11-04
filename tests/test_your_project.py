"""Test main cli"""
import aletheia.cli as cli

def test_get_message():
    assert cli.yo() == 'Yo cli!', 'cli.yo() returns "Yo cli!"'