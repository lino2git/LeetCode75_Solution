import pytest
from MergeStringsAlternately_1768 import mergeAlternately


# 正常案例測試
def test_equal_length():
    assert mergeAlternately("abc", "pqr") == "apbqcr"


def test_word2_longer():
    assert mergeAlternately("ab", "pqrs") == "apbqrs"


def test_word1_longer():
    assert mergeAlternately("abcd", "pq") == "apbqcd"


# 邊界與異常案例測試
def test_invalid_length_empty():
    with pytest.raises(ValueError, match="Length must be between 1 and 100."):
        mergeAlternately("", "pqr")


def test_invalid_special_characters():
    with pytest.raises(ValueError, match="Strings must contain only lowercase English letters."):
        mergeAlternately("abc!", "pqr")


def test_invalid_uppercase():
    with pytest.raises(ValueError, match="Strings must contain only lowercase English letters."):
        mergeAlternately("Abc", "pqr")