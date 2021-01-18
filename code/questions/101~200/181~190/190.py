"""
https://leetcode-cn.com/problems/reverse-bits
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        s = '0' * (32-len(s)) + s
        return int(s[::-1], 2)

print(
    Solution().reverseBits(
43261596
    )
)
