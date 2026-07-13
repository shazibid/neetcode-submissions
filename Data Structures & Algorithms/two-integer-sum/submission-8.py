class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for i, value in enumerate(nums):
            data[value] = i

        for i, value in enumerate(nums):
            num = target - value

            if num in data and data[num] != i:
                return [i, data[num]]