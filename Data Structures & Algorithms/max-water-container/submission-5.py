class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # result = 0
        # for left in range(len(heights)):
        #     for right in range(left+1, len(heights)):
        #         area = (right - left) * min(heights[left], heights[right])
        #         result = max(result, area)
        # return result
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            max_area = max(max_area, area)
        return max_area