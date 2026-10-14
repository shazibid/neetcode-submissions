class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            #base case: i == n, hasn't been seen before
            if len(nums) == len(path):
                res.append(path[:])
                return

            for i in nums:
                if i in path:
                    continue
                
                path.append(i)
                backtrack(path)
                path.pop()
        
        backtrack([])
        return res