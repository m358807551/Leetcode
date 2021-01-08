"""
https://leetcode-cn.com/problems/sort-colors/
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


s = [2,0,2,1,1,0, 1, 2, 1, 0, 1, 2, 0, 0]
Solution().sortColors(s)
print(s)
