class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        testing_arr = [')', '}', ']']
        for i in range(len(s)):
            if s[i] not in testing_arr:
                arr.push(s[i])
            else:
                while s[i] not in testing_arr:
                    arr.pop(s[i])
            
        return len(arr) == 0