class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1
        max_area = 0

        while left < right:
            max_area = max(min(height[left], height[right]) * (right - left), max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
