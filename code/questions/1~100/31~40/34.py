"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) -  1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return [-1, -1]
        start = left

        right = len(nums) - 1
        while left < right:
            mid = left + (right-left) // 2
            if target < nums[mid]:
                right = mid
            else:
                left += 1
        if nums[left] != target:
            return [start, left-1]
        else:
            return [start, left]



print(
    Solution().searchRange(
        nums=[5, 7, 7, 8, 8, 8, 9], target=8
    )
)
