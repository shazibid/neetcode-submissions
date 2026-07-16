class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] #creating pairs
        stack = []

        for p, s in sorted(pair)[::-1]: #(sorting by position)
            stack.append((target - p) / s) #calculate time it takes to get there

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #must check if theres 2 or more bc if only one we dont gaf
            #also check top by second top, if smaller, becomes a fleet
                stack.pop()
        
        return len(stack)
