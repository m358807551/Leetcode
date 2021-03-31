"""
https://leetcode-cn.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.res(l1, l2, 0)

    def res(self, h1, h2, i):
        if (h1 is h2 is None) and (i == 0):
            return None
        val = i
        if h1:
            val += h1.val
        if h2:
            val += h2.val
        head = ListNode(val % 10)
        head.next = self.res(h1.next if h1 else None, h2.next if h2 else None,  val // 10)
        return head


def main():
    nodes = [ListNode(num) for num in [2, 4, 3]]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    h1 = nodes[0]

    nodes = [ListNode(num) for num in [5, 6, 4]]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    h2 = nodes[0]
    rst = Solution().addTwoNumbers(h1, h2)
    print(rst)


if __name__ == '__main__':
    main()
