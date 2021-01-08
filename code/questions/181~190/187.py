"""
https://leetcode-cn.com/problems/repeated-dna-sequences
"""
from collections import defaultdict


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counts = defaultdict(int)
        for j in range(10, len(s)+1):
            counts[s[j-10: j]] += 1
        return [k for k, v in counts.items() if v > 1]


print(
    Solution().findRepeatedDnaSequences(
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    )
)
