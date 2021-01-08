"""
https://leetcode-cn.com/problems/generate-parentheses/
"""
from collections import defaultdict


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.rst = []
        self.backtrace([], n, n)
        return self.rst

    def backtrace(self, trace, left, right):
        if left == right == 0:
            self.rst.append(''.join(trace))
            return

        if left:
            trace.append('(')
            self.backtrace(trace, left-1, right)
            trace.pop(-1)

        if left < right:
            trace.append(')')
            self.backtrace(trace, left, right-1)
            trace.pop(-1)

print(
    Solution().generateParenthesis(3)
)
