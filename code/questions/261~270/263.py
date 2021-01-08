"""
https://leetcode-cn.com/problems/ugly-number
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        for i in [5, 3, 2]:
            if num % i == 0:
                return self.isUgly(num // i)
        return False


print(Solution().isUgly(
    2
))
