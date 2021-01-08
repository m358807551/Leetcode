"""
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or (nums[-1] < target):
            return len(nums)

        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


print(
    Solution().searchInsert(
[1,3,5,6], 3
    )
)
