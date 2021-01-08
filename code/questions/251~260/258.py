"""
https://leetcode-cn.com/problems/add-digits
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            new = 0
            while num:
                new += num % 10
                num //= 10
            num = new
        return num

print(
    Solution().addDigits(38)
)
