from collections import deque

class MyStack(object):

    def __init__(self):
        self.stack =  []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()