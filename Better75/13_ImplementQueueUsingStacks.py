class MyQueue(object):
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, x):  # O(1)
        """
        :type x: int
        :rtype: None
        """
        self.first_stack.append(x)

    def pop(self):  # O(1) amortized
        """
        :rtype: int
        """
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())

        return self.second_stack.pop() if self.second_stack else None

    def peek(self):  # O(1) amortized
        """
        :rtype: int
        """
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())

        return (
            self.second_stack[-1] if self.second_stack else None
        )  # Peek instead of popping

    def empty(self):  # O(1)
        """
        :rtype: bool
        """
        return not self.first_stack and not self.second_stack
