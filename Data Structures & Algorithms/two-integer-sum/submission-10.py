class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            d[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d and i != d[diff]:
                return [i, d[diff]]