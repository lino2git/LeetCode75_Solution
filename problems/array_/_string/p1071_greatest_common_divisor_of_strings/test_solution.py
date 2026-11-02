import pytest
from solution import Solution

@pytest.fixture
def sol():
    return Solution()

# 定義多個測試案例 (Test Cases)
def test_example_1(sol):
    assert sol.gcdOfStrings("ABCABC", "ABC") == "ABC"

def test_example_2(sol):
    assert sol.gcdOfStrings("ABABAB", "ABAB") == "AB"

def test_example_3(sol):
    assert sol.gcdOfStrings("LEET", "CODE") == ""

def test_example_4(sol):
    assert sol.gcdOfStrings("AAAAAB", "AAA") == ""