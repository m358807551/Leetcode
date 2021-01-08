"""
https://leetcode-cn.com/problems/3sum-smaller/
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rst = 0
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums)-1
            while left < right:
                value = nums[i] + nums[left] + nums[right]
                if value < target:
                    rst += right - left
                    left += 1
                else:
                    right -= 1
        return rst


print(
    Solution().threeSumSmaller(
nums = [-2,0,1,3], target = 2
    )
)
