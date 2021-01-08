"""
https://leetcode-cn.com/problems/course-schedule
"""
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.d = defaultdict(list)
        for cur, pre in prerequisites:
            self.d[pre].append(cur)

        self.points = [0] * numCourses
        for i, _ in enumerate(self.points):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.points[i] == 0:
            self.points[i] = 1
            for next in self.d[i]:
                if not self.dfs(next):
                    return False
            self.points[i] = 2
        elif self.points[i] == 1:
            return False

        return True

print(
    Solution().canFinish(
        2,
        [[1, 0]]

    )
)
