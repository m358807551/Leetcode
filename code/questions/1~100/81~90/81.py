"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] == nums[mid]:
                if nums[mid] == target:
                    return True
                left += 1
            elif nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return nums[left] == target


nums = [5, 1, 3]
target = 1
print(
    Solution().search(nums, target)
)
