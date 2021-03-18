"""
https://leetcode-cn.com/problems/largest-rectangle-in-histogram
"""


class Solution:
    def largestRectangleArea(self, heights):
        nums = [0] + heights + [0]
        stack = []
        rst = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                rst = max(rst, (i-stack[-2]-1) * nums[stack[-1]])
                stack.pop(-1)
            stack.append(i)
        return rst


nums = [2, 1, 2]
# nums = [2,1,5,6,2,3]


print(
    Solution().largestRectangleArea(nums)
)
