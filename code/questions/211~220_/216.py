"""
https://leetcode-cn.com/problems/combination-sum-iii
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.k, self.n = k, n
        self.rst = []
        self.backtrace([])
        return self.rst

    def backtrace(self, trace):
        if len(trace) == self.k:
            if sum(trace) == self.n:
                self.rst.append(trace[:])
            return
        start = trace[-1] + 1 if trace else 1
        for i in range(start, 10):
            trace.append(i)
            self.backtrace(trace)
            trace.pop(-1)

print(
    Solution().combinationSum3(
        3, 9
    )
)
