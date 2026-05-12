class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        return s == s[::-1]