"""
https://leetcode-cn.com/problems/wildcard-matching/
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[m][n]


print(
    Solution().isMatch(
        "adceb",
        "*a*b",
    )
)
