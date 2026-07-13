class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setter = set(nums)
        longest = 0

        for i, val in enumerate(nums):
            if val - 1 not in setter:
                length = 1
                while val + length in setter:
                    length += 1
            
                longest = max(longest, length)
        
        return longest

