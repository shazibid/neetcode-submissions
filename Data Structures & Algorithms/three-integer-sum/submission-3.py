class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        arr = []

        for a in range(len(nums) - 1):
            l = a + 1
            r = len(nums) - 1
            while l < r:
                cursum = nums[a] + nums[l] + nums[r]

                if cursum > 0:
                    r -= 1
                elif cursum < 0:
                    l += 1
                else:
                    if [nums[a], nums[l], nums[r]] not in arr:
                        arr.append([nums[a], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    
        
        return arr