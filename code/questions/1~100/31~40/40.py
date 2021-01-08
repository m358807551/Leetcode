"""
https://leetcode-cn.com/problems/combination-sum-ii/
"""

from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = Counter(candidates)
        self.rst = []
        self.backtrace([], d, target)
        return self.rst

    def backtrace(self, trace, d, target):
        if not target:
            if trace:
                self.rst.append(trace[:])
            return

        for num, count in list(d.items()):
            if count == 0:
                continue
            if num > target:
                continue
            if trace and trace[-1] > num:
                continue
            trace.append(num)
            d[num] -= 1
            self.backtrace(trace, d, target-num)
            trace.pop(-1)
            d[num] += 1


print(
    Solution().combinationSum2(
candidates = [2,5,2,1,2], target = 5,
    )
)
