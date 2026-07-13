class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # V = l * w
        #could use a value to store max V found

        maxV = 0

        for i in range(0, len(heights) - 1):
            for j in range(1, len(heights)):
                a = heights[i]
                b = heights[j]
                v = min(a, b) * abs(i - j)

                if v > maxV:
                    maxV = v
        
        return maxV
