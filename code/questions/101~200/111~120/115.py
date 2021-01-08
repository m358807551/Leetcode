"""
https://leetcode-cn.com/problems/distinct-subsequences
"""
from functools import lru_cache


class Solution(object):
    @lru_cache(None)
    def numDistinct(self, s, t):
        if not t:
            return 1
        rst = 0
        for i, letter in enumerate(s):
            if letter == t[0]:
               rst += self.numDistinct(s[i+1:], t[1:])
        return rst


print(
    Solution().numDistinct(
        'babgbag',
        'bag',
    )
)
