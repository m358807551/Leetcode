"""
https://leetcode-cn.com/problems/kth-largest-element-in-an-array
"""
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return -heapq.nsmallest(k, [-num for num in nums])[-1]


print(
    Solution().findKthLargest(
[3,2,1,5,6,4],k = 2
    )
)
