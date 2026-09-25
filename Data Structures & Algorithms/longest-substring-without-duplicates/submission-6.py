class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setty = set()
        l = 0
        maxl = 0

        for r in range(len(s)):
            while s[r] in setty:
                setty.remove(s[l])
                l += 1
            
            setty.add(s[r])
            maxl = max(maxl, r - l + 1)
        return maxl

