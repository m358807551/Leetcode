"""
https://leetcode-cn.com/problems/reverse-integer/
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rst = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return rst if -2**31<= rst <=2**31-1 else 0


print(
    Solution().reverse(
        1230
    )
)
