"""
https://leetcode-cn.com/problems/word-pattern/
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        d1, d2 = {}, {}
        for x, y in zip(pattern, str.split()):
            if d1.setdefault(x, y) != y or d2.setdefault(y, x) != x:
                return False
        return True


print(
    Solution().wordPattern(
        'abc',
        'b c a'
    )
)
