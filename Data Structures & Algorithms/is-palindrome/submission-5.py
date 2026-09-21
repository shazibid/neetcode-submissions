class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()

        newstr = "".join(char for char in s if char.isalnum())

        l, r = 0, len(newstr) - 1

        while l < r:
            if newstr[l] != newstr[r]:
                return False
            l += 1
            r -= 1
        return True