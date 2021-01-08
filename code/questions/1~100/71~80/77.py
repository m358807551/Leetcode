"""
https://leetcode-cn.com/problems/combinations
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        self.rst = []
        self.backtrace([])
        return self.rst

    def backtrace(self, trace):
        if len(trace) == self.k:
            self.rst.append(trace[:])
            return
        start = trace[-1] + 1 if trace else 1
        for num in range(start, self.n+1):
            trace.append(num)
            self.backtrace(trace)
            trace.pop()


print(
    Solution().combine(4, 2)
)
