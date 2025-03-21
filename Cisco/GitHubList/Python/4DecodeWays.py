from typing import Optional


class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        def is_valid(a: str, b: Optional[str] = None) -> bool:
            if b:
                return a == "1" or (a == "2" and b < "7")
            return a != "0"

        prevprev = 1
        prev = 1 if is_valid(s[-1]) else 0

        for i in reversed(range(N - 1)):
            curr = 0
            if is_valid(s[i]):
                curr += prev
            if is_valid(s[i], s[i + 1]):
                curr += prevprev

            prev, prevprev = curr, prev

        return prev
