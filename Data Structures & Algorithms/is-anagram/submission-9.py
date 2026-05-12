class Solution:
    # from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26
        for i in range(len(s)):
            arr[i] += ord(s[i]) - 97
            arr[i] -= ord(t[i]) - 97
        
        return all(x == 0 for x in arr)



            

        

