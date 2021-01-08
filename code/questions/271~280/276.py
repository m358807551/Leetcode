"""
https://leetcode-cn.com/problems/paint-fence/
"""


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1: 3] = [k, k*k]
        for i in range(3, len(dp)):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        return dp[n]


print(
    Solution().numWays(
        4, 2
    )
)
