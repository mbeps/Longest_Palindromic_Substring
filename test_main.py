import pytest
from main import Solution

def test_case_1():
    sol = Solution()
    assert sol.longestPalindrome("babad") == "bab"

def test_case_2():
    sol = Solution()
    assert sol.longestPalindrome("cbbd") == "bb"

def test_case_3():
    sol = Solution()
    assert sol.longestPalindrome("a") == "a"

def test_case_4():
    sol = Solution()
    assert sol.longestPalindrome("ac") == "a"

def test_case_5():
    sol = Solution()
    assert sol.longestPalindrome("racecar") == "racecar"

def test_case_6():
    sol = Solution()
    assert sol.longestPalindrome("abacdfgdcab") == "aba"

def test_case_7():
    sol = Solution()
    assert sol.longestPalindrome("madam") == "madam"

def test_case_8():
    sol = Solution()
    assert sol.longestPalindrome("bb") == "bb"

def test_case_9():
    sol = Solution()
    assert sol.longestPalindrome("abb") == "bb"
