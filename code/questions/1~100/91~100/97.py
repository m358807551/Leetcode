"""
https://leetcode-cn.com/problems/interleaving-string
"""
from functools import lru_cache


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.res(s1, s2, s3) or self.res(s2, s1, s3)

    @lru_cache(None)
    def res(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            return True
        for i in range(1, len(s1)+1):
            if s1[:i] == s3[:i]:
                if self.res(s2, s1[i:], s3[i:]):
                    return True
            else:
                break
        return False



print(
    Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
)
