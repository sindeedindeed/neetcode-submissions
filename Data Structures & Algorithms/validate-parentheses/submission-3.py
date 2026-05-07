class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        matches = {'(': ')', '{': '}', '[': ']'}

        for i in range(len(s)):
            if s[i] in matches:
                arr.append(s[i])
            else:
                if len(arr) == 0:
                    return False
                popped_bracket = arr.pop()
                if matches[popped_bracket] != s[i]:
                    return False

                
            
        return len(arr) == 0