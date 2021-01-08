"""
https://leetcode-cn.com/problems/palindrome-linked-list
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '[{}]'.format(self.val)


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or (not head.next):
            return True

        slow = fast = head
        slow_next = slow.next

        while fast and fast.next:
            fast = fast.next.next
            slow, slow_next.next, slow_next = slow_next, slow, slow_next.next

        if fast is None:
            if slow.val != slow.next.val:
                return False
            slow = slow.next.next
        else:
            slow = slow.next
        while slow_next:
            if slow_next.val != slow.val:
                return False
            slow = slow.next
            slow_next = slow_next.next

        return True


nodes = [ListNode(i) for i in [1, 2, 2, 1]]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

print(
    Solution().isPalindrome(nodes[0])
)
