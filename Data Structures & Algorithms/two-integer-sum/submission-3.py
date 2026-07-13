class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {} 

        for i, diff in enumerate(nums):
            data[diff] = i
            # i want the value to be the key and i to be our value
        
        

        for i, value in enumerate(nums):
            diff = target - value

            if diff in data:
                if data[diff] != i:
                    arr = [i, data[diff]]
                    return arr
