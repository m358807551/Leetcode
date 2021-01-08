"""
https://leetcode-cn.com/problems/sudoku-solver/
"""
from copy import deepcopy


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.rst = None
        self.backtrace(board, 0, 0)
        for r in range(9):
            for c in range(9):
                board[r][c] = self.rst[r][c]

    def backtrace(self, board, r, c):
        if self.rst:
            return
        if r > 8:
            self.rst = deepcopy(board)
            return

        if board[r][c] != '.':
            self.backtrace(board, r + c // 8, (c + 1) % 9)
        else:
            row_nums = set(board[r][j] for j in range(9) if board[r][j] != '.')
            col_nums = set(board[i][c] for i in range(9) if board[i][c] != '.')
            center_x, center_y = (r // 3)*3 + 1, (c // 3)*3 + 1
            center_nums = set()
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    x, y = center_x + i, center_y + j
                    if board[x][y] != '.':
                        center_nums.add(board[x][y])
            for num in set(list('123456789')) - row_nums - col_nums - center_nums:
                board[r][c] = num
                self.backtrace(board, r + c // 8, (c + 1) % 9)
                board[r][c] = '.'


def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Solution().solveSudoku(board)
    print(board)


if __name__ == '__main__':
    main()
