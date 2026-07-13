class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        length = r - l
        maxwater = length * min(heights[l], heights[r])

        while l < r:
            length = r - l
            water = length * min(heights[l], heights[r])

            if water > maxwater:
                maxwater = water

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maxwater


