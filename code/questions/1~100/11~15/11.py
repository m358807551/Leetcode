"""
https://leetcode-cn.com/problems/container-with-most-water/
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rst = 0
        left, right = 0, len(height)-1
        while left < right:
            rst = max(rst, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return rst
