"""
https://leetcode-cn.com/problems/find-median-from-data-stream/
"""
from heapq import heappush, heappop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.h1, -num)
        if self.h2 and (-self.h1[0] > self.h2[0]):
            heappush(self.h2, -heappop(self.h1))

        if len(self.h1) - len(self.h2) > 1:
            heappush(self.h2, -heappop(self.h1))

        if len(self.h2) > len(self.h1):
            heappush(self.h1, -heappop(self.h2))

    def findMedian(self):
        """
        :rtype: float
        """
        h1, h2 = self.h1, self.h2
        if len(h1) > len(h2):
            return -h1[0]
        else:
            return (-h1[0] + h2) / 2.0

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()

for x in [1, 2, 3]:
    obj.addNum(x)
print(obj.findMedian())
# param_2 = obj.findMedian()
