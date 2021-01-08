"""
https://leetcode-cn.com/problems/group-shifted-strings/
"""
from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        d = defaultdict(list)
        for string in strings:
            diss = []
            for i in range(1, len(string)):
                dis = ord(string[i]) - ord(string[i-1])
                dis = dis + 26 if dis < 0 else dis
                diss.append(dis)
            d[tuple(diss)].append(string)
        return list(d.values())

print(
    Solution().groupStrings(
["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    )
)
