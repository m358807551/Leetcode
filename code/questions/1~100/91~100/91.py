"""
https://leetcode-cn.com/problems/decode-ways
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [0] * n + [1, 1]
        for i in range(n):
            if s[i] != '0':
                dp[i] = dp[i-1]
            if i-1 >= 0 and '10' <= s[i-1: i+1] <= '26':
                dp[i] += dp[i-2]
        return dp[n-1]


print(
    Solution().numDecodings('111')
)
