"""
https://leetcode-cn.com/problems/flatten-2d-vector/
"""


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.arr = []
        for lis in v:
            self.arr.extend(lis)
        self.i = -1

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.arr[self.i]


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i != len(self.arr)-1


print(
    Vector2D([[1,2],[3],[4]]).next()
)
