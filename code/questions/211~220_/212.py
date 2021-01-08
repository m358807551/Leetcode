"""
https://leetcode-cn.com/problems/word-search-ii
"""
from collections import defaultdict
from copy import deepcopy


class Tire(object):
    def __init__(self):
        self.d = {}

    def add(self, word):
        d = self.d
        for letter in word:
            d = d.setdefault(letter, {})
        d['$'] = True

    def search(self, word):
        d = self.d
        for letter in word:
            d = d.get(letter)
            if not d:
                return False
        return d.get('$', False)

    def prefix(self, word):
        d = self.d
        for letter in word:
            d = d.get(letter)
            if not d:
                return False
        return True


class Solution(object):
    def findWords(self, board, words):
        self.rst = set()
        self.tire = Tire()
        for word in words:
            self.tire.add(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtrace('', board, i, j)

        return list(self.rst)

    def backtrace(self, trace, board, i, j):
        if self.tire.search(trace):
            self.rst.add(trace)

        if not(0 <= i < len(board) and   0<= j < len(board[0])):
            return

        if not self.tire.prefix(trace + board[i][j]):
            return

        letter = board[i][j]
        board[i][j] = '#'
        self.backtrace(trace+letter, board, i+1, j)
        self.backtrace(trace + letter, board, i - 1, j)
        self.backtrace(trace + letter, board, i, j+1)
        self.backtrace(trace+letter, board, i, j-1)
        board[i][j] = letter


print(
    Solution().findWords(
[['a']],
['a']
    )
)
