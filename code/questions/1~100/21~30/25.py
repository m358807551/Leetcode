"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        new_head, new_head_right, count = self.reverseK(head, k, 0)
        if count == k:
            head.next = self.reverseKGroup(new_head_right, k)
            return new_head
        else:
            rst, _, _ = self.reverseK(new_head, k, count)
            return rst

    def reverseK(self, head, k, count):
        if not head:
            return None, None, count
        if (not head.next) or k == 1:
            return head, head.next, count + 1
        new_head, new_head_right, count = self.reverseK(head.next, k-1, count+1)
        head.next.next = head
        head.next = new_head_right
        return new_head, new_head_right, count
