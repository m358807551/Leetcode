"""
https://leetcode-cn.com/problems/word-break-ii
"""

from functools import lru_cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.words = wordDict
        self.rst = []
        self.backtrace(s, [])
        return self.rst

    def backtrace(self, s, trace):
        if not s:
            self.rst.append(" ".join(trace))
            return
        for word in self.words:
            if s.startswith(word) and self.is_valid(s[len(word):]):
                trace.append(word)
                self.backtrace(s[len(word):], trace)
                trace.pop(-1)

    @lru_cache(None)
    def is_valid(self, s):
        if not s:
            return True
        for word in self.words:
            if s.startswith(word):
                if self.is_valid(s[len(word):]):
                    return True
        return False


a = "catsanddog"
b = ["cat","cats","and","sand","dog"]


print(
    Solution().wordBreak(a, b)
)
