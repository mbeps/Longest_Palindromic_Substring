class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * length for _ in range(length)]

        answer = ""
        # iterate the dp table in a bottom-up manner
        for chain_length in range(1, length + 1): 
            for i in range(length - chain_length + 1): 
                j = i + chain_length - 1
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]): 
                    dp[i][j] = True
                if dp[i][j] and (answer == "" or j - i + 1 > len(answer)):
                    answer = s[i:j+1]
        
        return answer
