"""
https://leetcode-cn.com/problems/shortest-word-distance-ii/
"""
from collections import defaultdict


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = defaultdict(list)

        for i, word in enumerate(words):
            self.d[word].append(i)

        for arr in self.d.values():
            arr.sort()

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rst = float('inf')
        for i in self.d[word1]:
            for j in self.d[word2]:
                rst = min(abs(i-j), rst)
        return rst


print(
    WordDistance(
["practice", "makes", "perfect", "coding", "makes"]
    ).shortest('makes', 'coding')
)

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
