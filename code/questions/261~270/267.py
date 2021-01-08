"""
https://leetcode-cn.com/problems/palindrome-permutation-ii/
"""
from collections import Counter


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = Counter(s)
        mid = ''
        for letter, count in d.items():
            if count % 2:
                if mid:
                    return []
                mid = letter
                d[mid] -= 1
                if not d[mid]:
                    d.pop(mid)
        self.rst = []
        self.backtrace(mid, d)
        return self.rst

    def backtrace(self, trace, d):
        if not d:
            self.rst.append(trace)
        for letter, count in d.items():
            d2 = {k: v for k, v in d.items()}
            d2[letter] -= 2
            if not d2[letter]:
                d2.pop(letter)
            self.backtrace(letter + trace + letter, d2)



print(
    Solution().generatePalindromes(
        'abab'
    )
)
