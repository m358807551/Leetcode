"""
https://leetcode-cn.com/problems/palindrome-partitioning-ii
"""

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        rst = float("inf")
        for i in range(1, len(s)):
            word = s[:i]
            if word == word[::-1]:
                rst = min(rst, 1+self.minCut(s[i:]))
        return rst


print(
    Solution().minCut(
        'aab'
    )
)
