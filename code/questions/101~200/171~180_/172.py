"""
https://leetcode-cn.com/problems/factorial-trailing-zeroes
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        return n//5 + self.trailingZeroes(n//5)
