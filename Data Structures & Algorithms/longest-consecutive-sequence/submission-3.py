class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setty = set()
        maxlen = 0

        for i in nums:
            setty.add(i)

        for i in nums:
            if i - 1 not in setty:
                length = 0

                while i+length in setty:
                    length += 1
                
                maxlen = max(length, maxlen)

                i = i + length + 1

        return maxlen
                
