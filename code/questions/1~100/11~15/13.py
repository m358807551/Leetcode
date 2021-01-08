"""
https://leetcode-cn.com/problems/roman-to-integer/
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rules = [
            (900, 'CM'),
            (400, 'CD'),
            (90, 'XC'),
            (40, 'XL'),
            (9, 'IX'),
            (4, 'IV'),
            (1000, 'M'),
            (500, 'D'),
            (100, 'C'),
            (50, 'L'),
            (10, 'X'),
            (5, 'V'),
            (1, 'I'),
        ]
        rst = 0
        i = 0
        while i < len(s):
            for x, y in rules:
                if s.startswith(y, i):
                    rst += x
                    i += len(y)
                    break
        return rst


print(
    Solution().romanToInt('MCMXCIV')
)
