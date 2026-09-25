class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setty = set()
        for i in nums:
            if i in setty:
                return True
            else:
                setty.add(i)
        return False
