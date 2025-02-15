class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_history = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.min_history:
            self.min_history.append(val)
        else:
            self.min_history.append(min(self.min_history[-1], val))

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            raise ValueError("Stack empty")

        self.stack.pop()
        self.min_history.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise ValueError("Stack empty")

        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise ValueError("Stack empty")

        return self.min_history[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
