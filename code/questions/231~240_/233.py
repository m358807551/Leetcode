"""
https://leetcode-cn.com/problems/number-of-digit-one
"""


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        rst = 0
        while n >= k:
            rst += n//(10*k) * k + min(k, max(0, n % (10*k) - k + 1))
            k *= 10
        return rst


print(
    Solution().countDigitOne(1)
)
