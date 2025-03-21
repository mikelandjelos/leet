class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                cur = []
                while stack and stack[-1] != "[":
                    cur.append(stack.pop())
                stack.pop()  # Remove '['

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                mul = int("".join(num[::-1]))

                stack.extend(cur[::-1] * mul)
        return "".join(stack)
