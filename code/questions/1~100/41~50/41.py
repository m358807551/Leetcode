"""
https://leetcode-cn.com/problems/first-missing-positive/
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 0)
        for i in range(len(nums)):
            while (
                (1 <= nums[i] <= len(nums) - 1)
                and nums[i] != nums[nums[i]]
            ):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

print(
    Solution().firstMissingPositive(
        [1, 2]
    )
)
