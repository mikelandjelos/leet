from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROTTEN, HEALTHY = 2, 1
        height, width = len(grid), len(grid[0])

        rotting_oranges = deque()
        total_oranges = 0

        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element != 0:  # If the element is orange.
                    total_oranges += 1
                    if element == ROTTEN:
                        rotting_oranges.append((i, j))

        minutes = 0
        rotten_count = len(rotting_oranges)

        while rotting_oranges:
            level_size = len(rotting_oranges)

            for _ in range(level_size):  # Level order traversal.
                r, c = rotting_oranges.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] == HEALTHY:
                        grid[nr][nc] = ROTTEN  # Rot the orange.
                        rotting_oranges.append((nr, nc))
                        rotten_count += 1

            # Minute == processed level.
            if rotting_oranges:
                minutes += 1

        return minutes if rotten_count == total_oranges else -1
