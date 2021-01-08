"""
https://leetcode-cn.com/problems/word-search/
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return len(word) == 0
        self.rst = False
        self.board = board
        self.word = word
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.backtrace(r, c, set(), 0)
        return self.rst


    def backtrace(self, r, c, trace, i):
        if self.rst:
            return
        if i == len(self.word):
            self.rst = True
            return
        if not (0 <= r < len(self.board) and 0 <= c < len(self.board[0])):
            return
        if self.board[r][c] != self.word[i]:
            return
        for a, b in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            r2, c2 = r + a, c + b
            if (r2, c2) in trace:
                continue
            trace |= {(r, c)}
            self.backtrace(r2, c2, trace, i+1)
            trace -= {(r, c)}


bb = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
from pprint import pprint
a = Solution().exist(bb, "ABCB")
pprint(a)
