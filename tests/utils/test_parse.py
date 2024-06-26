"""Unit tests for parsing-related functions."""

from agential.utils.parse import (
    normalize_answer,
    remove_articles,
    remove_newline,
    remove_punc,
    white_space_fix,
)


def test_remove_newline() -> None:
    """Test remove_newline function."""
    step = "\n  Step with extra spaces and newlines \n"
    assert remove_newline(step) == "Step with extra spaces and newlines"

    # Test with internal newlines.
    step = "Step\nwith\ninternal\nnewlines"
    assert remove_newline(step) == "Stepwithinternalnewlines"

    # Test with a string that doesn't require formatting.
    step = "Already formatted step"
    assert remove_newline(step) == "Already formatted step"


def test_remove_articles() -> None:
    """Test remove_articles function."""
    sample_text = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )

    result = remove_articles(sample_text)
    expected = (
        "A fox jumped over   fence. An apple was on   table. The quick brown fox."
    )
    assert result == expected, f"Test failed: Expected '{expected}', got '{result}'"


def test_white_space_fix() -> None:
    """Test white_space_fix function."""
    sample_text = "over   fence"
    result = white_space_fix(sample_text)
    assert result == "over fence"


def test_remove_punc() -> None:
    """Test remove_punc function."""
    sample_text = "abcd.,"
    result = remove_punc(sample_text)
    assert result == "abcd"


def test_normalize_answer() -> None:
    """Test normalize_answer function."""
    sample_text = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )

    result = normalize_answer(sample_text)
    expected = "fox jumped over fence apple was on table quick brown fox"
    assert result == expected
