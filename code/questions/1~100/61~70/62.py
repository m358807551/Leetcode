"""
https://leetcode-cn.com/problems/unique-paths
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [
            [1] * n
            for _ in range(m)
        ]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

print(
    Solution().uniquePaths(23, 12)
)
