class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        right = 0

        for right in range(len(s)):
            if s[right] not in chars:
                chars[s[right]] = right
            else:
                left = chars[s[right]] + 1
                chars[s[right]] = right

            max_length = right - left + 1
        return max_length

