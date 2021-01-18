"""
https://leetcode-cn.com/problems/rotate-array
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        self.reverse(0, n-k-1)
        self.reverse(n-k, n-1)
        self.reverse(0, n-1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


nums = [1,2,3,4,5,6,7]
Solution().rotate(
    nums,
    3
)
print(nums)
