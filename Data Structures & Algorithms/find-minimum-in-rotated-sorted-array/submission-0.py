class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        small = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(small, nums[l])
            
            m = (l + r) // 2

            small = min(small, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return small
