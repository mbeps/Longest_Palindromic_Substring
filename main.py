class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(s: str) -> str:
            return s == s[::-1]

        longest: str = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring: str = s[i:j]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
