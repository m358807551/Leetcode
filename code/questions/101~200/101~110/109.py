"""
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.res(head, None)

    def res(self, left, right):
        """左闭右开."""
        if left is right:
            return None

        slow = fast = left
        while (fast is not right) and (fast.next is not right):
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow)
        root.left = self.res(left, slow)
        root.right = self.res(slow.next, right)
        return root

