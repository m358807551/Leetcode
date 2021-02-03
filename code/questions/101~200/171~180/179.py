"""
https://leetcode-cn.com/problems/largest-number
"""

from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        rst = sorted(map(str, nums), key=cmp_to_key(lambda a, b: -1 if a+b < b+a else 1), reverse=True)
        return ''.join(rst) if rst[0] != '0' else '0'


print(
    Solution().largestNumber(
            # [3,30,34,5,9]
            [34, 9]
    )
)
