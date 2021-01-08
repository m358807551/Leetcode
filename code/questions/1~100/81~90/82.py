"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = thead = ListNode(None)
        p = thead.next = head
        while p:
            if left.next is p:
                pass
            elif p.val == left.next.val:
                pass
            elif left.next.next is p:
                left = left.next
            else:
                left.next = p
            p = p.next
        if left and left.next and left.next.next:
            left.next = None
        return thead.next

a = [
    ListNode(1),
    # ListNode(1),
    ListNode(2),
    ListNode(3),
    ListNode(3),
    ListNode(4),
    ListNode(4),
    # ListNode(4),
    ListNode(5),
    ListNode(5),
    ListNode(5),
]

for i in range(len(a)-1):
    a[i].next = a[i+1]

h = Solution().deleteDuplicates(a[0])
p = h
while p:
    print(p.val)
    p = p.next
