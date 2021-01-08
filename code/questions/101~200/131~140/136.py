"""
https://leetcode-cn.com/problems/single-number
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        for num in nums:
            rst ^= num
        return rst



print(
    Solution().singleNumber(
[4,1,2,1,2]
    )
)
