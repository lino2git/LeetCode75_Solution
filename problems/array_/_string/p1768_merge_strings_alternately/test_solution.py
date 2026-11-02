import pytest
from solution import Solution

@pytest.fixture
def sol():
    return Solution()

# 正常案例測試
def test_equal_length(sol):
    assert sol.mergeAlternately("abc", "pqr") == "apbqcr"


def test_word2_longer(sol):
    assert sol.mergeAlternately("ab", "pqrs") == "apbqrs"


def test_word1_longer(sol):
    assert sol.mergeAlternately("abcd", "pq") == "apbqcd"


# 邊界與異常案例測試
def test_invalid_length_empty(sol):
    with pytest.raises(ValueError, match="Length must be between 1 and 100."):
        sol.mergeAlternately("", "pqr")


def test_invalid_special_characters(sol):
    with pytest.raises(ValueError, match="Strings must contain only lowercase English letters."):
        sol.mergeAlternately("abc!", "pqr")


def test_invalid_uppercase(sol):
    with pytest.raises(ValueError, match="Strings must contain only lowercase English letters."):
        sol.mergeAlternately("Abc", "pqr")