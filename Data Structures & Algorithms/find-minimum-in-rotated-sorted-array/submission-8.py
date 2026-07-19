class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = 0
        while nums[l] > nums[r]:
            m = l + ((r - l) // 2)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
            
        
        return nums[l]