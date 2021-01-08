"""
https://leetcode-cn.com/problems/sort-list
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.val)


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head
        h1 = fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        slow.next = None

        h1 = self.sortList(h1)
        h2 = self.sortList(h2)

        th = tail = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
                tail = tail.next
            else:
                tail.next = h2
                h2 = h2.next
                tail = tail.next
        tail.next = h1 or h2

        return th.next


def main():
    nodes = [ListNode(i) for i in range(5)]
    nodes[4].next = nodes[2]
    nodes[2].next = nodes[1]
    nodes[1].next = nodes[3]

    p = Solution().sortList(nodes[4])
    while p:
        print(p, )
        p = p.next


if __name__ == '__main__':
    main()
