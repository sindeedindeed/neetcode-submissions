class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counts = Counter(nums)
        for x in nums:
            if counts[x] > 1:
                return True
        return False