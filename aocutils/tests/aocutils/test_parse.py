import pytest
from unittest.mock import mock_open, patch
import re

from aocutils import Parser  # TODO: not use relative import


@pytest.fixture
def sample_text():
    return """Line 1
Line 2

Section 1
Section 1continued

Line 3
Line 4
"""


def test_init_with_file(sample_text):
    with patch("builtins.open", mock_open(read_data=sample_text)):
        parser = Parser(file_name="test.txt")
    assert parser.data == sample_text.strip()


def test_init_with_text(sample_text):
    parser = Parser(text=sample_text)
    assert parser.data == sample_text.strip()


def test_init_with_both_file_and_text():
    with pytest.raises(
        ValueError, match="Only one of file_name or text must be provided"
    ):
        Parser(file_name="test.txt", text="Sample text")


def test_get_lines(sample_text):
    parser = Parser(text=sample_text)
    assert parser.get_lines() == [
        "Line 1",
        "Line 2",
        "",
        "Section 1",
        "Section 1continued",
        "",
        "Line 3",
        "Line 4",
    ]


def test_get_sections(sample_text):
    parser = Parser(text=sample_text)
    assert parser.get_sections() == [
        "Line 1\nLine 2",
        "Section 1\nSection 1continued",
        "Line 3\nLine 4",
    ]


def test_get_grid(sample_text):
    parser = Parser(text=sample_text)
    grid = parser.get_grid()
    assert grid.content == [
        ["Line", "1"],
        ["Line", "2"],
        ["Section", "1"],
        ["Section", "1continued"],
        ["Line", "3"],
        ["Line", "4"],
    ]


def test_apply_regex(sample_text):
    parser = Parser(text=sample_text)
    pattern = r"Line (\d+)"
    matches = parser.apply_regex(pattern)
    assert matches == [["1"], ["2"], [], [], [], [], ["3"], ["4"]]

    pattern = r"Line \d+"
    matches = parser.apply_regex(pattern)
    assert matches == [["Line 1"], ["Line 2"], [], [], [], [], ["Line 3"], ["Line 4"]]


def test_apply_regex_with_location(sample_text):
    parser = Parser(text=sample_text)
    pattern = r"Line (\d+)"
    matches = parser.apply_regex(pattern, return_loc=True)
    print(matches)
    match = matches[0]
    print(len(match))
    print(match)
    print(match[0])
    assert len(matches) == 8
    assert all(isinstance(m, list) for m in matches)
    for line_matches in matches:
        assert all(isinstance(m, re.Match) for m in line_matches)
