"""
https://leetcode-cn.com/problems/word-ladder
"""

from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList) | {beginWord}
        pat2words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + '_' + word[i+1:]
                pat2words[pat].append(word)
        adj = defaultdict(list)
        for words in pat2words.values():
            for i in range(len(words)):
                adj[words[i]].extend(words[:i] + words[i+1:])

        queue = {beginWord}
        visited = {beginWord}
        parents = defaultdict(list)
        while queue:
            if endWord in queue:
                break

            visited |= queue
            queue = {
                parents[child].append(node) or child
                for node in queue
                for child in adj[node]
                if child not in visited
            }
        rst = 1
        cur = endWord
        while cur != beginWord:
            if not parents[cur]:
                return 0
            cur = parents[cur][0]
            rst += 1
        return rst


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(
        Solution().ladderLength(beginWord, endWord, wordList)
    )


if __name__ == '__main__':
    main()
