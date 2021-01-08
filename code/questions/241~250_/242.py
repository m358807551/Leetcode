"""
https://leetcode-cn.com/problems/valid-anagram
"""
from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
