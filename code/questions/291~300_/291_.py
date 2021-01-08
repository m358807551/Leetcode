"""
https://leetcode-cn.com/problems/word-pattern-ii/
"""


class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.pattern = pattern
        self.rst = False
        self.backtrace([], str)
        return self.rst

    def is_valid(self, pattern, trace):
        if len(pattern) != len(trace):
            return False
        d1, d2 = {}, {}
        for x, y in zip(pattern, trace):
            if d1.setdefault(x, y) != y or d2.setdefault(y, x) != x:
                return False
        return True

    def backtrace(self, trace, s):
        if self.rst:
            return
        if not s:
            if self.is_valid(self.pattern, trace):
                self.rst = True
            return

        if trace:
            if len(trace) == len(self.pattern):
                t = trace[-1]
                trace[-1] += s
                self.backtrace(trace, '')
                trace[-1] = t
            else:
                trace.append(s[0])
                self.backtrace(trace, s[1:])
                trace.pop(-1)

                if len(s) > len(self.pattern) - len(trace):
                    trace[-1] += s[0]
                    self.backtrace(trace, s[1:])
                    trace[-1] = trace[: -1]
        else:
            if len(self.pattern) == 1:
                trace.append(s)
                self.backtrace(trace, '')
                trace.pop(-1)
            else:
                trace.append(s[0])
                self.backtrace(trace, s[1:])
                trace.pop(-1)

print(
    Solution().wordPatternMatch(
        pattern="abab", str="redblueredblue"
    )
)
