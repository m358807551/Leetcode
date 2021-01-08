"""
https://leetcode-cn.com/problems/implement-queue-using-stacks
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        t = []
        while self.stack:
            t.append(self.stack.pop(-1))
        self.stack.append(x)
        while t:
            self.stack.append(t.pop(-1))

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
