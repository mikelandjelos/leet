class Solution:
    def isValid(self, s: str) -> bool:
        closed_opened = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        lifo = []
        for br in s:
            if br in ("[", "(", "{"):
                lifo.append(br)
            else:
                if len(lifo) == 0 or closed_opened[br] != lifo.pop():
                    return False

        return True if len(lifo) == 0 else False
