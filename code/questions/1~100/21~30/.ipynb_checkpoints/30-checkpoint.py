"""
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
"""
from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        target = defaultdict(int)
        for word in words:
            target[word] += 1
        m = len(words[0])
        rst = []
        for k in range(m):
            s_cut = [s[i: i+m] for i in range(k, len(s), m)]
            d = defaultdict(int)
            queue = []
            for i, word in enumerate(s_cut):
                if word not in target:
                    d = defaultdict(int)
                    queue = []
                else:
                    while queue and d[word] == target[word]:
                        d[s_cut[queue.pop(0)]] -= 1
                    queue.append(i)
                    d[word] += 1

                    if d == target:
                        rst.append(queue[0] * m + k)
        return rst


print(
    Solution().findSubstring(
        s="barfoothefoobarman",
        words=["foo", "bar"]
    )
)
