"""
https://leetcode-cn.com/problems/string-to-integer-atoi/
"""
import re

INT_MIN = -2**31
INT_MAX = 2**31 - 1


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        match = re.match('[+-]?\d+', str.lstrip())
        if not match:
            return 0
        rst = int(match.group())
        if rst < INT_MIN:
            return INT_MIN
        if rst > INT_MAX:
            return INT_MAX
        return rst


print(
    Solution().myAtoi(
        '  -123A'
    )
)
