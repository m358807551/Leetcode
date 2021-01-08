"""
https://leetcode-cn.com/problems/unique-binary-search-trees
"""
from functools import lru_cache


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.res(1, n)

    @lru_cache(None)
    def res(self, left, right):
        if left >= right:
            return 1
        rst = 0
        for i in range(left, right+1):
            n_left_tress = self.res(left, i-1)
            n_right_tress = self.res(i+1, right)
            rst += n_left_tress * n_right_tress
        return rst


print(
    Solution().numTrees(19)
)
