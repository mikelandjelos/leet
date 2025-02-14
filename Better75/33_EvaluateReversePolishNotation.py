class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        q = []
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(float(x) / y),
        }

        for token in tokens:
            if token in "+-*/":
                second = q.pop()
                first = q.pop()
                q.append(operations[token](first, second))
            else:
                q.append(int(token))

        return q.pop()
