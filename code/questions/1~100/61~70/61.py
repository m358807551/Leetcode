"""
https://leetcode-cn.com/problems/rotate-list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        n, p = 0, head
        while p:
            p = p.next
            n += 1

        k = k % n
        p1 = p2 = head
        for _ in range(k):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = head
        rst = p1.next
        p1.next = None
        return rst


def main():
    head = ListNode(1)
    print(Solution().rotateRight(head, 1))


if __name__ == '__main__':
    main()
