class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            #base case: if combination adds to target and combo hasn't been seen
            summy = 0
            for j in path:
                summy += j
                if summy > target:
                    break
            
            if i >= len(nums) or summy > target:
                return
            
            if summy == target:
                res.append(path[:])
                return
            
            #decision 1: to add itself
            path.append(nums[i])
            backtrack(i, path)
            path.pop()

            #decision 2: to not add itself
            backtrack(i + 1, path)
        
        backtrack(0, [])

        return res