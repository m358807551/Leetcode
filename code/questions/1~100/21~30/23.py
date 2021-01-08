"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) % 2:
            lists.append(None)
        if len(lists) == 2:
            return self.merge2(*lists)
        mid = len(lists) // 2
        a = self.mergeKLists(lists[: mid])
        b = self.mergeKLists(lists[mid:])
        return self.merge2(a, b)

    def merge2(self, h1, h2):
        if h1 is h2 is None:
            return None
        if (not h1) or (h2 and h1.val > h2.val):
            h1, h2 = h2, h1
        h1.next = self.merge2(h1.next, h2)
        return h1
