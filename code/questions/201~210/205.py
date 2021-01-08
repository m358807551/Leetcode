"""
https://leetcode-cn.com/problems/isomorphic-strings
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.index, s)) == list(map(t.index, t))


print(
    Solution().isIsomorphic(
        'ab',
        'cd'
    )
)
