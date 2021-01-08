"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = t = ListNode(None)
        t.next = head
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return t.next
