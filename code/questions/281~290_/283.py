"""
https://leetcode-cn.com/problems/move-zeroes
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                if right != left:
                    nums[left], nums[right] = nums[right], 0
                left += 1
        return nums

print(
    Solution().moveZeroes(
        [0, 1, 0, 3, 12]
    )
)
