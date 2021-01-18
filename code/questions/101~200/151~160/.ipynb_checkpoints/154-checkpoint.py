"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]

print(
    Solution().findMin(
[10,1,10,10,10]
    )
)
