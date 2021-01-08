"""
https://leetcode-cn.com/problems/happy-number
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while n not in d:
            d.add(n)
            n = self.f(n)
        return n == 1

    def f(self, n):
        rst = 0
        while n:
            rst += (n % 10) * (n % 10)
            n //= 10
        return rst


print(Solution().isHappy(2))
