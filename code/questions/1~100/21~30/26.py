"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        for num in nums:
            if num != nums[left]:
                left += 1
                nums[left] = num
        return left + 1


a = [1, 1, 2, 3, 3, 4, 5, 5]
print(
    Solution().removeDuplicates(
        a
    )
)
print(a)
