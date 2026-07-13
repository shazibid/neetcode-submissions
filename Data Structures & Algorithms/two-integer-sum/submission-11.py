class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, val in enumerate(nums):
            d[val] = i
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in d and i != d[diff]:
                return [i, d[diff]]