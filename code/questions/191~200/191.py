"""
https://leetcode-cn.com/problems/number-of-1-bits
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        while n:
            rst += n & 1
            n >>= 1
        return rst


print(
    Solution().hammingWeight(11)
)
