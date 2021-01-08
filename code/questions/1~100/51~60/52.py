# coding=utf-8

"""
https://leetcode-cn.com/problems/n-queens-ii
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.rst = 0
        board = [
            ['.'] * n
            for _ in range(n)
        ]
        self.backtrace(board, 0)
        return self.rst

    def backtrace(self, board, row):
        if row >= len(board):
            self.rst += 1
            return

        for c in range(len(board)):
            if self.is_valid(board, row, c):
                board[row][c] = 'Q'
                self.backtrace(board, row+1)
                board[row][c] = '.'

    def is_valid(self, board, r, c):
        # 左上
        i, j = r-1, c-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j-1

        # 上
        i = r-1
        while i >= 0:
            if board[i][c] == 'Q':
                return False
            i -= 1

        # 右上
        i, j = r-1, c+1
        while i >= 0 and j <= len(board)-1:
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j+1
        return True


print(
    Solution().totalNQueens(4)
)
