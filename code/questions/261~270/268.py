"""
https://leetcode-cn.com/problems/missing-number/
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        for i in range(len(nums)+1):
            rst ^= i
        for num in nums:
            rst ^= num
        return rst


print(
    Solution().missingNumber(
        [0,2, 3]
    )
)
