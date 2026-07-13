class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dictionary that counts how many times a value appears (first string)
        #with second string drop the count per each time a value appears
            #if count < 0; return false
            #if letter dne; return false
            #else return true
        
        checker = {}

        for i in s:
            if i not in checker:
                checker[i] = 1
            else:
                checker[i] += 1
                
        for i in t:
            if i not in checker:
                return False
            
            checker[i] -= 1

            if checker[i] < 0:
                return False
        
        for i in checker:
            if checker[i] != 0:
                return False

        return True