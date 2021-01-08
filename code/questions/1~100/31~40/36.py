"""
https://leetcode-cn.com/problems/valid-sudoku/
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            nums = [board[row][col] for col in range(9) if board[row][col] != '.']
            if len(nums) != len(set(nums)):
                return False

        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != '.']
            if len(nums) != len(set(nums)):
                return False

        for row in (1, 4, 7):
            for col in (1, 4, 7):
                nums = []
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        x = row + i
                        y = col + j
                        if board[x][y] == '.':
                            continue
                        nums.append(board[x][y])
                if len(nums) != len(set(nums)):
                    return False
        return True


print(
    Solution().isValidSudoku(
        [
[".", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", ".", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
)
)
