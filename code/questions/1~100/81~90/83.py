"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
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
        if not head or (not head.next):
            return head

        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return head


head = tail = None
nums = [1, 1, 1, 2, 3, 3]
for num in  nums:
    if not head:
        head = tail = ListNode(num)
    else:
        tail.next = ListNode(num)
        tail = tail.next

h = Solution().deleteDuplicates(head)
p = h
while p:
    print(p.val)
    p = p.next
