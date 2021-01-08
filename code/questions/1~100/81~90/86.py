"""
https://leetcode-cn.com/problems/partition-list
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = t1 = ListNode(None)
        h2 = t2 = ListNode(None)
        p = head
        while p:
            if p.val < x:
                t1.next = p
                t1 = t1.next
            else:
                t2.next = p
                t2 = t2.next
            p = p.next
        t1.next = h2.next
        t2.next = None
        return h1.next


head = tail = None
nums = [1, 4, 3, 2, 5, 2]
for num in nums:
    if not head:
        head = tail = ListNode(num)
    else:
        tail.next = ListNode(num)
        tail = tail.next

h = Solution().partition(head, 3)
p = h
while p:
    print(p.val)
    p = p.next
