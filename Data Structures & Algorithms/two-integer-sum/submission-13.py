class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in d and d[diff] != i:
                return [d[diff], i]
            
            d[val] = i