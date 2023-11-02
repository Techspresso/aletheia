"""Test main cli"""
import your_project.cli as cli

def test_get_message():
    assert cli.yo() == 'Yo cli!', 'cli.yo() returns "Yo cli!"'