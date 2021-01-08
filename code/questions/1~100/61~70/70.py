"""
https://leetcode-cn.com/problems/climbing-stairs
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


print(
    Solution().climbStairs(10)
)
