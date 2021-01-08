"""
https://leetcode-cn.com/problems/rectangle-area
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if F >= D or C <= E or B >= H or G <= A:
            return (D-B)*(C-A) + (H-F)*(G-E)

        a = sorted([A, C, E, G])
        b = sorted([H, F, D, B])
        return        (D-B)*(C-A) + (H-F)*(G-E) - (a[2]-a[1])*(b[2]-b[1])
