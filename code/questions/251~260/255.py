"""
https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/
"""


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack, max_popup = [], float('-inf')
        for num in preorder:
            if num < max_popup:
                return False
            while stack and stack[-1] < num:
                max_popup = max(max_popup, stack.pop(-1))
            stack.append(num)
        return True



print(
    Solution().verifyPreorder(
[5, 2, 6, 1, 3]
    )
)
