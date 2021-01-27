"""
https://leetcode-cn.com/problems/one-edit-distance/
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 找到第一个不同的地方
        for i in range(min(
            len(s),
            len(t),
        )):
            if s[i] != t[i]:
                return (
                    (s[:i]+s[i+1:]) == (t[:i]+t[i+1:]) or
                    (s[:i]+s[i+1:]) == t or
                    (s == t[:i]+t[i+1:])
                )

        return abs(len(s) - len(t)) == 1


print(
    Solution().isOneEditDistance(
        '1203',
        '1213'
    )
)
