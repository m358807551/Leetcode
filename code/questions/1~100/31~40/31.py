"""
https://leetcode-cn.com/problems/next-permutation/
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        queue = []
        for j in range(len(nums)-1, -1, -1):
            if queue and nums[j] < nums[queue[-1]]:
                break
            queue = [j]
        j = queue[-1]
        if j == 0:
            left, right = 0, len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return

        queue = []
        i = j - 1
        for k in range(j, len(nums)):
            if nums[k] <= nums[i]:
                continue
            if not queue:
                queue = [k]
            elif nums[k] < nums[queue[-1]]:
                queue = [k]

        k = queue[0]
        nums[i], nums[k] = nums[k], nums[i]
        nums[j:] = sorted(nums[j:])


s = [1,1]
print(
    Solution().nextPermutation(
        s
    )
)
print(s)
