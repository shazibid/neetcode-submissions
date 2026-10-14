class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #index = which number being currently decided
        #path = current subset being built (list)
        def backtracking(index, path):
            #base case -- leaf of tree
            if index == len(nums):
                res.append(path[:])
                return
            
            #decision 1: include nums[index]
            #ie to include the number we are currently looking at
            path.append(nums[index])
            backtracking(index + 1, path)
            path.pop()

            #decision 2: dont include index
            backtracking(index + 1, path)
        
        backtracking(0, [])
        return res
