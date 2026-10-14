class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            #base case
            if i == len(nums):
                res.append(path[:])
                return
            
            #decision 1: to include
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            #decision 2: to not include
            backtrack(i + 1, path)

        backtrack(0, [])
        return res
