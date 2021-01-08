"""
https://leetcode-cn.com/problems/sliding-window-maximum
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = []
        rst = []
        for num in nums:
            if len(queue) < k:
                queue.append(num)
            else:
                rst.append(max(queue))
                queue.pop(0)
                queue.append(num)
        rst.append(max(queue))
        return rst
