"""
https://leetcode-cn.com/problems/palindrome-permutation/
"""
from collections import defaultdict


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = defaultdict(int)
        for letter in s:
            if d[letter]:
                d.pop(letter)
            else:
                d[letter] = 1
        return len(d) < 2



print(
    Solution().canPermutePalindrome(
'aabbaab'
    )
)

