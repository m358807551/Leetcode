"""
https://leetcode-cn.com/problems/shortest-word-distance/
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rst, stack = float('inf'), []
        for i, word in enumerate(words):
            if word not in {word1, word2}:
                continue
            if stack and words[stack[-1]] != word:
                rst = min(rst, i-stack[-1])
            stack.append(i)

        return rst
