class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for i in nums:
            if i not in nums2:
                nums2.add(i)
            else:
                return True
        
        return False