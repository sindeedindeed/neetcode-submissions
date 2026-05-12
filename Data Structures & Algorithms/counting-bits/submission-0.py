class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = 0
        while n:
            bits += 1
            n &= n - 1
        return bits