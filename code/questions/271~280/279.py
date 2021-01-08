"""
https://leetcode-cn.com/problems/perfect-squares
"""
import math


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        dp = [0] * (n+1)
        for num in range(1, n+1):
            sqrt = num ** 0.5
            if sqrt == int(sqrt):
                dp[num] = 1
                continue
            dp[num] = min(1 + dp[num-i*i] for i in range(1, int(sqrt)+1))
        return dp[n]


print(
    Solution().numSquares(
        13
    )
)
