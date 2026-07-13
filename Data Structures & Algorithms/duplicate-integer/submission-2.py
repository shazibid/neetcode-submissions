class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = set()

        for i in nums:
            if i not in data:
                data.add(i)
            else:
                return True
        
        return False