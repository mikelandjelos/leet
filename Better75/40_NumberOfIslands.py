class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        TAG = "#"
        count = 0
        height, width = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element != "1":
                    continue

                count += 1
                q = [(i, j)]

                while q:
                    r, c = q.pop()
                    grid[r][c] = TAG

                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        nr, nc = r + dx, c + dy

                        if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] == "1":
                            q.append((nr, nc))

        return count
