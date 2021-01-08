"""
https://leetcode-cn.com/problems/word-break
"""
from functools import lru_cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.words = wordDict
        return self.res(s)

    @lru_cache(None)
    def res(self, s):
        if not s:
            return True
        for word in self.words:
            if s.startswith(word):
                if self.res(s[len(word):]):
                    return True
        return False




s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat", 'og']


print(
    Solution().wordBreak(
        s,
        wordDict
    )
)
