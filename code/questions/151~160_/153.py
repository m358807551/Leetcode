"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
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
            mid = left + (right-left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


print(
    Solution().findMin(
[2, 1]
    )
)
