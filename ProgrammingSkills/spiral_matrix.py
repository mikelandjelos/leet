class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        result = []

        while True:
            # Left to right.
            for num in matrix[top][left : right + 1]:
                result.append(num)
            top += 1

            if top > bottom:
                break

            # Top to bottom.
            for num in map(lambda x: x[right], matrix[top : bottom + 1]):
                result.append(num)
            right -= 1

            if right < left:
                break

            # Right to left.
            for num in reversed(matrix[bottom][left : right + 1]):
                result.append(num)
            bottom -= 1

            if bottom < top:
                break

            # Bottom to top.
            for num in map(lambda x: x[left], reversed(matrix[top : bottom + 1])):
                result.append(num)
            left += 1

            if left > right:
                break

        return result
