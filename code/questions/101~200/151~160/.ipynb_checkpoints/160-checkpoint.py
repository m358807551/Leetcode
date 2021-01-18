"""
https://leetcode-cn.com/problems/intersection-of-two-linked-lists
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or (not headB):
            return None

        p1, count1 = headA, 1
        p2, count2 = headB, 1

        while p1.next:
            p1 = p1.next
            count1 += 1

        while p2.next:
            p2 = p2.next
            count2 += 1

        if p1 is not p2:
            return None

        if count1 < count2:
            headA, headB = headB, headA

        for _ in range(abs(count2 - count1)):
            headA = headA.next

        while headA is not headB:
            headA = headA.next
            headB = headB.next


        return headB
