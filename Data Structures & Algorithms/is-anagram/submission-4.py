class Solution:
    # from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26
        for i in range(len(s)):
            ele1 = ord(s[i])
            arr[ele1] += 1

        for j in range(len(t)):
            ele2 = ord(t[j])
            if ele2 > -1:
                arr[ele2] -= 1
            else:
                return False
        
        return True



            

        

