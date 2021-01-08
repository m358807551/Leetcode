"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = j = 0
        for k in range(1, len(nums)):
            if nums[k] == nums[j]:
                if i == j:
                    nums[j+1] = nums[k]
                    j += 1
            else:
                nums[j+1] = nums[k]
                j += 1
                i = j
        return j + 1


nums = [0,0,1,1,1,1,2,3,3,3]
x = Solution().removeDuplicates(nums)
print(nums[: x])
