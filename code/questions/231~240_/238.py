"""
https://leetcode-cn.com/problems/product-of-array-except-self
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst, p, q = [1], 1, 1
        for i in range(1, len(nums)):
            p *= nums[i-1]
            rst.append(p)
        for j in range(len(nums)-2, -1, -1):
            q *= nums[j+1]
            rst[j] *= q
        return rst


print(
    Solution().productExceptSelf(
        [0, 0]
    )
)
