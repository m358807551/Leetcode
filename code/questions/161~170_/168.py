"""
https://leetcode-cn.com/problems/excel-sheet-column-title
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        rst = ''
        while n:
            n -= 1
            rst += chr(65 + n % 26)
            n //= 26
        return rst[::-1]


print(
    Solution().convertToTitle(27)
)
