class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        starting_color = image[sr][sc]
        q = [(sr, sc)]

        if starting_color == color:
            return image

        while len(q) > 0:
            r, c = q.pop()
            image[r][c] = color

            # Top.
            if r - 1 >= 0 and image[r - 1][c] == starting_color:
                q.append((r - 1, c))

            # Right.
            if c + 1 < len(image[0]) and image[r][c + 1] == starting_color:
                q.append((r, c + 1))

            # Left.
            if c - 1 >= 0 and image[r][c - 1] == starting_color:
                q.append((r, c - 1))

            # Bottom.
            if r + 1 < len(image) and image[r + 1][c] == starting_color:
                q.append((r + 1, c))

        return image
