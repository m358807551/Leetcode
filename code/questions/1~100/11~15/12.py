"""
https://leetcode-cn.com/problems/integer-to-roman/
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rules = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        rst = ''
        while num > 0:
            for x, y in rules:
                if num >= x:
                    num -= x
                    rst += y
                    break
        return rst


print(
    Solution().intToRoman(
        1994
    )
)
