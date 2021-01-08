"""
https://leetcode-cn.com/problems/linked-list-cycle-ii
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                p = head
                while p is not slow:
                    p = p.next
                    slow = slow.next
                return p
