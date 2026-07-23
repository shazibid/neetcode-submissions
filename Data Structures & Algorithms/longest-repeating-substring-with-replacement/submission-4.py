class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxL = 0

        alphabet = {}

        for r in range(len(s)):
            alphabet[s[r]] = 1 + alphabet.get(s[r], 0)

            while (r - l + 1) - max(alphabet.values()) > k:
                alphabet[s[l]] -= 1
                l += 1
        

            maxL = max(maxL, r - l + 1)
        
        return maxL