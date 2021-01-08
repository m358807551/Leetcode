"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""
from functools import lru_cache


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        if k >= len(prices) // 2:
            k = float('inf')
        return self.res(len(prices)-1, k, 0)

    @lru_cache(None)
    def res(self, i, k, is_hold):
        if k <= 0:
            return 0
        if i < 0 and not is_hold:
            return 0
        elif i < 0 and is_hold:
            return float('-inf')

        if is_hold:
            return max(
                self.res(i-1, k-1, 0) - self.prices[i],
                self.res(i-1, k, 1),
            )
        else:
            return max(
                self.res(i-1, k, 1) + self.prices[i],
                self.res(i-1, k, 0)
            )


print(
    Solution().maxProfit(
        2,
        [3, 2, 6, 5, 0, 3]
    )
)
