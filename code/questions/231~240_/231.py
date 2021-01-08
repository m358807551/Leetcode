"""
https://leetcode-cn.com/problems/power-of-two
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n-1) == 0


print(
    Solution().isPowerOfTwo(0)
)
