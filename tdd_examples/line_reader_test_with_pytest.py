import os
import pytest
from pytest import raises
from unittest.mock import MagicMock


def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File")
    infile = open(filename, "r")
    line = infile.readline()
    return line


"""
Test
"""
@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)

    return mock_open

def test_returns_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = read_from_file("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"


def test_throws_exception_with_bad_file(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = read_from_file("blah")

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
