"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
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
            for _ in range(5)
        ]

        dp[1][n-1] = dp[3][n-1] = prices[n-1]
        for j in range(n-2, -1, -1):
            for i in range(4):
                cost = prices[j] if i in [1, 3] else -prices[j]
                dp[i][j] = max(
                    dp[i][j+1],
                    dp[i+1][j+1] + cost
                )

        return dp[0][0]


if __name__ == '__main__':
    nums = [3,3,5,0,0,3,1,4]
    print(
        Solution().maxProfit(nums)
    )

