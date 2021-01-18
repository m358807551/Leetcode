"""
https://leetcode-cn.com/problems/maximum-gap
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums.sort()
        rst = float('-inf')
        for i in range(1, len(nums)):
            rst = max(rst, nums[i] - nums[i-1])
        return rst


print(
    Solution().maximumGap(1)
)
