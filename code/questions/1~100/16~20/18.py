"""
https://leetcode-cn.com/problems/4sum/
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        rst = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum4 == target:
                        rst.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                    elif sum4 < target:
                        left += 1
                    else:
                        right -= 1
        return list(rst)

print(
    Solution().fourSum(
nums = [1, 0, -1, 0, -2, 2], target = 0
    )
)
