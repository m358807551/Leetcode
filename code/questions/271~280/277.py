"""
https://leetcode-cn.com/problems/find-the-celebrity/
"""


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        for j in range(1, n):
            if knows(i, j):
                i = j

        for j in range(n):
            if i == j:
                continue
            if knows(i, j) or (not knows(j, i)):
                return -1
        return i
