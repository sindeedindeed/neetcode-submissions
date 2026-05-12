class Solution:
    # from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26
        for i in range(len(s)):
            arr[int(s[i])] += 1

        for j in range(len(t)):
            ele = int(t[i])
            if ele > -1:
                arr[ele] -= 1
            else:
                return False
        
        return True



            

        

