class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setter = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in setter:
                length = 0
                while (i + length) in setter:
                    length += 1
                longest = max(length, longest)
        
        return longest