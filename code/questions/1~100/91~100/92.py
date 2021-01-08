"""
https://leetcode-cn.com/problems/reverse-linked-list-ii
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
            return self.reverse_k(head, n)
        else:
            head.next = self.reverseBetween(head.next, m-1, n-1)
            return head

    def reverse_k(self, head, n):
        if n == 1:
            self.suc = head.next
            return head

        new_head = self.reverse_k(head.next, n-1)
        head.next.next = head
        head.next = self.suc
        return new_head


def main():
    head = tail = None
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        if not head:
            head = tail = ListNode(num)
        else:
            tail.next = ListNode(num)
            tail = tail.next

    h = Solution().reverseBetween(head, 2, 4)
    p = h
    while p:
        print(p.val)
        p = p.next


if __name__ == '__main__':
    main()
