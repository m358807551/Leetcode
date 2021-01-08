"""
https://leetcode-cn.com/problems/course-schedule-ii
"""
from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.d = defaultdict(list)
        for cur, pre in prerequisites:
            self.d[pre].append(cur)

        self.rst = []
        self.points = [0] * numCourses
        for i, _ in enumerate(self.points):
            if not self.dfs(i):
                return []
        return self.rst[::-1]

    def dfs(self, i):
        if self.points[i] == 0:
            self.points[i] = 1
            for next in self.d[i]:
                if not self.dfs(next):
                    return False
            self.points[i] = 2
            self.rst.append(i)
        elif self.points[i] == 1:
            return False

        return True


print(

)
