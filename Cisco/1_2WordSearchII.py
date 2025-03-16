class TrieNode:
    def __init__(self, end: bool = False):
        self.children = {}
        self.end = -1


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Construct Trie
        trie = TrieNode()
        for index, word in enumerate(words):
            cur = trie
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.end = index

        M, N = len(board), len(board[0])
        DIRECTIONS = [
            (0, 1),  # Right
            (0, -1),  # Left
            (-1, 0),  # Up
            (1, 0),  # Down
        ]
        result = []

        def dfs(i: int, j: int, trie: TrieNode):
            if trie.end != -1:
                result.append(words[trie.end])
                trie.end = -1  # Big Brain move :)

            if i >= M or i < 0 or j >= N or j < 0 or board[i][j] not in trie.children:
                return

            temp, board[i][j] = board[i][j], "#"

            for di, dj in DIRECTIONS:
                dfs(i + di, j + dj, trie.children[temp])

            board[i][j] = temp

        for i in range(M):
            for j in range(N):
                dfs(i, j, trie)

        return result
