class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]
        maxR = [0]

        maxH = 0

        for i in range(0, len(height)):
            maxH = max(height[i], maxH)
            maxL.append(maxH)

        maxH = 0

        for i in range(len(height) - 1, -1, -1):
            maxH = max(height[i], maxH)
            maxR.insert(0, maxH)
        
        print(maxL, maxR)
        total = 0

        minH = []

        for i in range(len(height)):
            mini = min(maxL[i], maxR[i]) - height[i]
            if mini >= 0:   
                total += mini
        

        
        return total
        
