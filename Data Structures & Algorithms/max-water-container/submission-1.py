class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # V = l * w
        #could use a value to store max V found

        l = 0
        r = len(heights) - 1
        max_v = 0

        while l < r: #two pointer method
            v = min(heights[l], heights[r]) * (r - l)
            if v > max_v:
                max_v = v
            
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return max_v

