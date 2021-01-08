"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[left] > nums[right]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                break

        start = left

        if nums[start] <= target <= nums[-1]:
            left, right = start, len(nums)-1
        else:
            left, right = 0, start-1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

print(
    Solution().search(
        [6, 5, 1, 2, 3, 4],
        3
    )
)
