"""
https://leetcode-cn.com/problems/sqrtx
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left, right = 0, x
        while left < right:
            mid = left + (right-left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1

print(
    Solution().mySqrt(5)
)
