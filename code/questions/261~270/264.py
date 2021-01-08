"""
https://leetcode-cn.com/problems/ugly-number-ii/
"""
import heapq
import operator


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [1, 2]
        rst = None
        for _ in range(n):
            while operator.eq(*heapq.nsmallest(2, queue)):
                heapq.heappop(queue)
            rst = heapq.heappop(queue)
            heapq.heappush(queue, rst*2)
            heapq.heappush(queue, rst*3)
            heapq.heappush(queue, rst*5)
        return rst


print(
    Solution().nthUglyNumber(10)
)
