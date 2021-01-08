"""
https://leetcode-cn.com/problems/permutation-sequence
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = [str(i) for i in range(1, n+1)]
        k -= 1
        rst = ''
        while arr and k:
            t = self.fac(len(arr)-1)
            rst += arr.pop(k//t)
            k %= t

        rst += ''.join(arr)
        return rst

    def fac(self, n):
        rst = 1
        for i in range(1, n+1):
            rst *= i
        return rst

print(
    Solution().getPermutation(3, 2)
)
