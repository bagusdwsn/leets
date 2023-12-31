class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the width and height of the current container
            width = right - left
            current_height = min(height[left], height[right])

            # Calculate the area of the current container and update max_area
            max_area = max(max_area, width * current_height)

            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
