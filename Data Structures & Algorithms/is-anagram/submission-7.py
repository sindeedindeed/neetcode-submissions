class Solution:
    # from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26
        for i in range(len(s)):
            ele1 = ord(s[i]) - 97
            arr[ele1] += 1

        for j in range(len(t)):
            ele2 = ord(t[j]) - 97
            arr[ele2] -= 1
        
        return all(x == 0 for x in arr)



            

        

