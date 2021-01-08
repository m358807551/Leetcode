"""
https://leetcode-cn.com/problems/subsets-ii
"""
from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = Counter(nums)
        rst = [[]]
        for num, times in d.items():
            t = []
            for i in range(1, times+1):
                t.extend([x+[num]*i for x in rst])
            rst.extend(t)
        return rst


print(
    Solution().subsetsWithDup([1, 2, 2])
)
