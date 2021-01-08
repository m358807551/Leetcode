"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [
            [0] * n
            for _ in range(3)
        ]
        dp[1][n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            dp[0][i] = max(
                -prices[i] + dp[1][i+1],
                dp[0][i+1],
            )
            dp[1][i] = max(
                dp[1][i+1],
                prices[i] + dp[2][i+1],
            )

        return dp[0][0]


print(
    # Solution().maxProfit([7,1,5,3,6,4])
    Solution().maxProfit([2,7,1,9])
)
