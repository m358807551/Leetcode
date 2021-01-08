"""
https://leetcode-cn.com/problems/group-anagrams/
"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for str_ in strs:
            d[tuple(sorted(str_))].append(str_)

        return list(d.values())


print(
    Solution().groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    )
)
