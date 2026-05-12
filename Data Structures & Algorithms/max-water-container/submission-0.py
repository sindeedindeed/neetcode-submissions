class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = max(heights)
        max_index = heights.index(max_height)
        max_area = 0
        for i in range(len(heights)):
            water_area = heights[i] * abs(max_index - i)
            if water_area > max_area:
                max_area = water_area
            
        return max_area