"""
https://leetcode-cn.com/problems/copy-list-with-random-pointer
"""

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old2new = {None: None}
        cur = head
        while cur:
            old2new[cur] = Node(cur.val)
            cur = cur.next

        old = head
        while old:
            old2new[old].next = old2new[old.next]
            old2new[old].random = old2new[old.random]
            old = old.next

        return old2new[head]
