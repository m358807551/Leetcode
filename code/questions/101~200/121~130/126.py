"""
https://leetcode-cn.com/problems/word-ladder-ii
"""
from collections import defaultdict


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        pat2words = defaultdict(list)
        wordList = set(wordList) | {beginWord}
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + '_' + word[i+1:]
                pat2words[pat].append(word)
        get_children = defaultdict(list)
        for nodes in pat2words.values():
            for i in range(len(nodes)):
                get_children[nodes[i]].extend(nodes[:i] + nodes[i+1:])

        queue = {beginWord}
        visited = {beginWord}
        get_parents = defaultdict(list)
        while queue:
            # print(queue)
            visited |= queue
            queue = {
                get_parents[child].append(node) or child
                for node in queue
                for child in get_children[node]
                if child not in visited
            }

        self.rst = []
        self.get_parents = get_parents
        self.begin_word = beginWord
        self.backtrace([endWord])
        # print(1)
        return self.rst

    def backtrace(self, trace):
        if trace[-1] == self.begin_word:
            self.rst.append(trace[::-1])
            return
        for parent in self.get_parents[trace[-1]]:
            trace.append(parent)
            self.backtrace(trace)
            trace.pop(-1)


def main():
    """测试入口."""
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    rst = Solution().findLadders(
        beginWord,
        endWord,
        wordList,
    )
    for line in rst:
        print(' '.join(line))


if __name__ == '__main__':
    main()
