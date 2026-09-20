class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hi = set()

        for i in nums:
            if i in hi:
                return True
            hi.add(i)
        
        return False