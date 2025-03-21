class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        M, N, W = len(board), len(board[0]), len(word)
        DIRECTIONS = [
            (0, 1),  # Right
            (0, -1),  # Left
            (-1, 0),  # Up
            (1, 0),  # Down
        ]

        def dfs(i: int, j: int, target: int) -> bool:  # O(4**L) time, O(L) space
            if target == W:
                return True

            if i >= M or i < 0 or j >= N or j < 0 or board[i][j] != word[target]:
                return False

            temp, board[i][j] = board[i][j], "#"  # Mark as visited

            for di, dj in DIRECTIONS:
                if dfs(i + di, j + dj, target + 1):
                    return True

            board[i][j] = temp
            return False

        # Word can begin from anywhere.
        for i in range(M):  # O(M)
            for j in range(N):  # O(N)
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True
        return False
