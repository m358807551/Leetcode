"""
https://leetcode-cn.com/problems/maximal-rectangle
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rst = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            line = matrix[i]
            for j in range(n):
                if line[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            rst = max(rst, self.help(heights))
        return rst

    def help(self, heights):
        heights = [0] + heights + [0]
        stack = []
        rst = 0
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                rst = max(rst, (i-stack[-2]-1) * heights[stack[-1]])
                stack.pop(-1)
            stack.append(i)
        return rst

s = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(
    # Solution().maximalRectangle(s)
    Solution().help([3, 1, 3, 2, 2])
)
