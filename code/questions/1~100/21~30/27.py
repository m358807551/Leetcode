"""
https://leetcode-cn.com/problems/remove-element/
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = -1
        for num in nums:
            if num != val:
                left += 1
                nums[left] = num
        return left + 1
