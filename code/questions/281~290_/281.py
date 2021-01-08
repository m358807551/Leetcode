"""
https://leetcode-cn.com/problems/zigzag-iterator/
"""


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.arr = [v1, v2]

    def next(self):
        """
        :rtype: int
        """
        if not self.arr[0]:
            self.arr = self.arr[::-1]
        rst = self.arr[0].pop(0)
        self.arr = self.arr[::-1]
        return rst

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.arr != [[], []]


print(
    ZigzagIterator(
v1 = [1,2],
v2 = [3,4,5,6]
    ).next()
)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
