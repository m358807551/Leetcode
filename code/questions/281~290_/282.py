"""
https://leetcode-cn.com/problems/expression-add-operators/
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.rst = []
        self.target = target
        self.backtrace('', num)
        return self.rst

    def backtrace(self, trace, s):
        if not s:
            if trace:
                if eval(trace) == self.target:
                    self.rst.append(trace)
            return

        if not trace:
            self.backtrace(trace+s[0], s[1:])
        else:
            i = len(trace) - 1
            while 0 <= i and trace[i] == '0':
                i -= 1
            if not (i < 0 or trace[i] in '+-*'):
                self.backtrace(trace+s[0], s[1:])

            self.backtrace(trace + '+' + s[0], s[1:])
            self.backtrace(trace + '-' + s[0], s[1:])
            self.backtrace(trace + '*' + s[0], s[1:])


print(
    Solution().addOperators(
        '00',
        0
    )
)
