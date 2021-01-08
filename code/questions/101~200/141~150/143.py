"""
https://leetcode-cn.com/problems/reorder-list
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        # 链表长度为0或1，就啥也不用干
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        slow.next = None

        h2 = self.reverse(h2)

        self.combine(head, h2)

    def reverse(self, head):
        if (not head) or (not head.next):
            return head
        rst = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rst

    def combine(self, h1, h2):
        if not h2:
            return h1
        t = self.combine(h1.next, h2.next)
        h1.next = h2
        h2.next = t
        return h1


def main():
    nodes = [ListNode(i) for i in range(6)]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[4].next = nodes[5]
    rst = Solution().reorderList(nodes[1])
    print(rst)


if __name__ == '__main__':
    main()
