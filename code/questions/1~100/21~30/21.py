"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is l2 is None:
            return None
        if (not l1) or (l1 and l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
