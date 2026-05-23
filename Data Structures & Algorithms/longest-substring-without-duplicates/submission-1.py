class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = {}
        count = 0
        for char in s:
            if char not in set1:
                set1.add(char)
                count += 1
        return count

            
        