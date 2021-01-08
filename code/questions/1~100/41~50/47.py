"""
https://leetcode-cn.com/problems/permutations-ii/
"""
from collections import defaultdict


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        self.rst = []
        self.backtrace([], d)
        return self.rst

    def backtrace(self, trace, d):
        if not d:
            self.rst.append(trace[:])
            return

        for num, times in list(d.items()):
            trace.append(num)
            d[num] -= 1
            if d[num] == 0:
                del d[num]
            self.backtrace(trace, d)
            trace.pop(-1)
            d[num] += 1


print(
    Solution().permuteUnique([1, 1, 2])
)
