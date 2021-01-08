"""
https://leetcode-cn.com/problems/maximal-square
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix))]
        rst = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '1':
                    continue
                step = 0
                while (j-step >= 0 and i-step >= 0) and (matrix[i][j-step] == matrix[i-step][j] == '1'):
                    step += 1
                dp[i][j] = min(step-1, dp[i-1][j-1]) + 1
                rst = max(rst, dp[i][j])

        return rst * rst


lines = """
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
"""
matrix = [line.split() for line in lines.strip().split('\n')]
# matrix = [
#     ["0","0","0","1"],
#     ["1","1","0","1"],
#     ["1","1","1","1"],
#     ["0","1","1","1"],
#     ["0","1","1","1"]]
print(
    Solution().maximalSquare(
        []
    )
)
