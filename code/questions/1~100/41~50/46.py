"""
https://leetcode-cn.com/problems/permutations/
"""
from collections import defaultdict


class Solution(object):
    def permute(self, nums):
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

        for k in list(d.keys()):
            trace.append(k)
            d[k] -= 1
            if not d[k]:
                del d[k]
            self.backtrace(trace, d)
            trace.pop(-1)
            d[k] += 1


print(
    Solution().permute([1, 2, 3])
)
