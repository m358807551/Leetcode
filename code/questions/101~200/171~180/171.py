"""
https://leetcode-cn.com/problems/excel-sheet-column-number/
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        for ch in s:
            num = ord(ch) - ord('A') + 1
            rst = rst * 26 + num
        return rst


print(
    Solution().titleToNumber('ZY')
)
