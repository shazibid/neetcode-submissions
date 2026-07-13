class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        #if difference is in array, then output the associated position
        for i in range(len(nums)):
            diff[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in diff and diff[difference] != i:
                return [i, diff[difference]]