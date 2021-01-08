"""
https://leetcode-cn.com/problems/insertion-sort-list
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.val)


class Solution(object):
    def insertionSortList(self, head):
        th = ListNode(0)

        p2 = head
        while p2:
            p2_next = p2.next

            p1 = th
            while p1.next and p1.next.val < p2.val:
                p1 = p1.next
            p2.next = p1.next
            p1.next = p2

            p2 = p2_next

        return th.next


def main():
    nodes = [ListNode(i) for i in range(5)]
    nodes[4].next = nodes[2]
    nodes[2].next = nodes[1]
    nodes[1].next = nodes[3]

    p = Solution().insertionSortList(nodes[4])
    while p:
        print(p, )
        p = p.next


if __name__ == '__main__':
    main()
