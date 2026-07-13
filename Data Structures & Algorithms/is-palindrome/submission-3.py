class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        i = 0
        j = len(s) - 1
        s = s.lower()

        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and j > i:
                j -= 1
            
            if s[i] != s[j]:
                return False
            j -= 1
            i += 1

        return True