class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicty = {}

        for i in range(len(nums)):
            dicty[nums[i]] = i
        
        for i in range(len(nums)):
            num = target - nums[i]

            if num in dicty and dicty[num] != i:
                return [i, dicty[num]]

            

        return []