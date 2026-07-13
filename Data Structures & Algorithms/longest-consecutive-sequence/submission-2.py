class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if 
        setting = set()
        maxl = 0

        for i in nums:
            setting.add(i)
        
        for i in nums:
            if i - 1 not in setting:
                length = 0

                while i + length in setting:
                    length += 1
                
                if length > maxl:
                    maxl = length
                
                i = i + length + 1
        
        return maxl
    
