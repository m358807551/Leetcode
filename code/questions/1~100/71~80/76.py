"""
https://leetcode-cn.com/problems/minimum-window-substring
"""
from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = right = 0
        tt, d, dd = defaultdict(int), defaultdict(int), defaultdict(int)
        i, j = None, None
        for x in t:
            tt[x] += 1
        while True:
            while right < len(s) and dd != tt:
                letter = s[right]
                right += 1
                if letter not in tt:
                    continue
                d[letter] += 1
                dd[letter] = min(d[letter], tt[letter])

            if dd != tt:
                break

            while dd == tt:
                letter = s[left]
                left += 1
                if letter not in tt:
                    continue
                d[letter] -= 1
                dd[letter] = min(d[letter], tt[letter])
            if i is None or right - left + 1 < j - i:
                i, j = left - 1, right
        return '' if i is None else s[i: j]


print(
    Solution().minWindow("a", "aa")
)
