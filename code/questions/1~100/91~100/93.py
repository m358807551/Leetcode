"""
https://leetcode-cn.com/problems/restore-ip-addresses
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        self.rst = []
        self.backtrace([], s)
        return self.rst

    def backtrace(self, trace, s):
        n = len(trace)
        if not (4-n <= len(s) <= 3*(4-n)):
            return
        if len(trace) == 4:
            self.rst.append('.'.join(trace))
            return

        if len(s) >= 1:
            trace.append(s[0])
            self.backtrace(trace, s[1:])
            trace.pop(-1)

        if int(s[:2]) >= 10:
            trace.append(s[:2])
            self.backtrace(trace, s[2:])
            trace.pop(-1)

        if 100 <= int(s[:3]) <= 255:
            trace.append(s[:3])
            self.backtrace(trace, s[3:])
            trace.pop(-1)


def main():
    s = '11111'
    # s = '25525511135'
    print(
        Solution().restoreIpAddresses(s)
    )


if __name__ == '__main__':
    main()
