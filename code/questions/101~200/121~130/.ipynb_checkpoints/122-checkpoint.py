"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rst = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                rst += prices[i+1] - prices[i]
        return rst


print(
    Solution().maxProfit([7,1,5,3,6,4])
)
