"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        p = head.next
        p.next, head.next = head, self.swapPairs(p.next)
        return p
