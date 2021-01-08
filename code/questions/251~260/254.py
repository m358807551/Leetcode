"""
https://leetcode-cn.com/problems/factor-combinations/
"""
import math


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.rst = []
        self.backtrace([], n)
        return self.rst

    def backtrace(self, trace, n):
        if trace:
            self.rst.append(trace + [n])

        for i in range(trace[-1] if trace else 2, int(math.sqrt(n))+1):
            if n % i == 0:
                trace.append(i)
                self.backtrace(trace, n // i)
                trace.pop(-1)


print(
    Solution().getFactors(
        23848713,
        # 8,
    )
)
