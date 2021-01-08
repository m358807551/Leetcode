"""
https://leetcode-cn.com/problems/remove-linked-list-elements
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        t_head = ListNode(None)
        t_head.next = head
        self.res(t_head, head, val)
        return t_head.next

    def res(self, pre, cur, val):
        if not cur:
            return
        if cur.val == val:
            pre.next = cur.next
            self.res(pre, cur.next, val)
        else:
            self.res(cur, cur.next, val)
