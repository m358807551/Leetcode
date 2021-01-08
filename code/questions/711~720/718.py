"""
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
"""
from pprint import pprint


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        self.A = A
        self.B = B
        dp = [
            [0] * len(B)
            for _ in range(len(A))
        ]
        dp[0][0] = 1 if A[0] == B[0] else 0
        for i in range(1, len(A)):
            dp[i][0] = 1 if A[i] == B[0] else 0
        for j in range(1, len(B)):
            dp[0][j] = 1 if A[0] == B[j] else 0

        rst = 0
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                dp[i][j] = 1 + dp[i-1][j-1] if A[i] == B[j] else 0
                rst = max(rst, dp[i][j])

        return rst


pprint(
    Solution().findLength(
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    )
)
