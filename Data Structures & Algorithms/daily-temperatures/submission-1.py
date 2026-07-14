class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #iterate from the end
        #stack descending
        #pushing to the stack: curr is smaller than top
        #tuples to associate index to temp
        #subtract 

        stack = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if len(stack) > 0:
                #one element exists bigger than the current element
                diff = stack[-1][1] - i
                res.append(diff)
            
            else:
                res.append(0)

                
            stack.append([temperatures[i], i])

        
        return res[::-1]




        