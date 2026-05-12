class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalnum() is False:
                i += 1
            if s[j].isalnum() is False:
                j -= 1
            if s[i] != s[j]:
                return False
        return True
