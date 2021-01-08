"""
https://leetcode-cn.com/problems/min-stack/
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.temp = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        t = []
        while self.temp and self.temp[-1] > x:
            t.append(self.temp.pop(-1))
        self.temp.append(x)
        while t:
            self.temp.append(t.pop(-1))

        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop(-1)
        self.temp.remove(x)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.temp[0]

# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   # --> 返回 -3.
minStack.pop()
minStack.top()      # --> 返回 0.
minStack.getMin()   # --> 返回 -2.

print(1)
