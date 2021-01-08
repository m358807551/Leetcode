"""
https://leetcode-cn.com/problems/alien-dictionary/
"""
from collections import defaultdict
from functools import reduce
import operator


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        adj = defaultdict(list)
        for i in range(1, len(words)):
            A, B = words[i-1],  words[i]
            for j in range(min(len(A), len(B))):
                if A[j] != B[j]:
                    adj[A[j]].append(B[j])
                    break
            else:
                if j == len(B)-1 and len(B) < len(A):
                    return ''
        rst = ''
        while adj:
            starts = set(adj) - set(reduce(operator.add, adj.values()))
            if not starts:
                return ''

            for start in starts:
                rst += start
                adj.pop(start)

        return rst + ''.join(set(''.join(words))-set(rst))

print(
    Solution().alienOrder(
[
  "abc",
  "ab"
]
    )
)
