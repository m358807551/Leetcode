"""
https://leetcode-cn.com/problems/palindrome-partitioning
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        self.rst = []
        self.backtrace([], s)
        return self.rst

    def backtrace(self, trace, s):
        if not s:
            self.rst.append(trace[:])
        for i in range(1, len(s)+1):
            word = s[:i]
            if word == word[::-1]:
                trace.append(word)
                self.backtrace(trace, s[i:])
                trace.pop(-1)


print(
    Solution().partition(
        'aab'
    )
)
