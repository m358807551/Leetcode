"""
https://leetcode-cn.com/problems/scramble-string

todo: 改造成正儿八经的动态规划
"""
from functools import lru_cache


class Solution(object):
    @lru_cache(None)
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        n = len(s1)
        if n == 1:
            return False
        for i in range(1, n):
            if self.isScramble(s1[: i], s2[: i]) and self.isScramble(s1[i: ], s2[i: ]):
                return True
            if self.isScramble(s1[: i], s2[-i: ]) and self.isScramble(s1[i: ], s2[: -i]):
                return True
        return False

print(
    Solution().isScramble(
        "abcdefghijklmnopq",
        "efghijklmnopqcadb"
    )
)
