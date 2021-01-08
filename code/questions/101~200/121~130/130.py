"""
https://leetcode-cn.com/problems/surrounded-regions
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        def bfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'A'
                bfs(i-1, j)
                bfs(i+1, j)
                bfs(i, j-1)
                bfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if i in (0, m-1) or j in (0, n-1):
                    bfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'




board = [
    ["O", "O", "O", "O", "X", "X"],
    ["O", "O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "O", "O"]
]

Solution().solve(board)

for line in board:
    print(line)
