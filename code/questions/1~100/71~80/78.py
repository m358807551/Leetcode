"""
https://leetcode-cn.com/problems/subsets
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        for num in nums:
            rst.extend([x + [num] for x in rst])
        return rst


print(
    Solution().subsets([7, 8, 9])
)
