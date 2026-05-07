class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        closing_arr = [')', '}', ']']
        matches = {'(': ')', '{': '}', '[': ']'}

        for i in range(len(s)):
            if s[i] in closing_arr:
                if len(arr) == 0:
                    return False
                popped_bracket = arr.pop()
                if matches[popped_bracket] != s[i]:
                    return False
            else:
                arr.append(s[i])
                
            
        return len(arr) == 0