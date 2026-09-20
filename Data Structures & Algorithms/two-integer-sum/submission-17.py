class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicty = {}

        for i in range(len(nums)):
            dicty[nums[i]] = i
        
        for i in range(len(nums)):
            hi = target - nums[i]

            if hi in dicty and dicty[hi] != i:
                return [i, dicty[hi]]