"""
https://leetcode-cn.com/problems/maximum-product-subarray
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reversed_nums = nums[::-1]
        for i in range(1, len(nums)):
            reversed_nums[i] *= reversed_nums[i-1] or 1
            nums[i] *= nums[i-1] or 1
        return max(reversed_nums + nums)
