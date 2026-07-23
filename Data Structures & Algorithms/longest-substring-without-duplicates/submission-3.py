class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0
        string = set()

        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l += 1
            string .add(s[r])

            maxL = max(maxL, r - l + 1)

        return maxL