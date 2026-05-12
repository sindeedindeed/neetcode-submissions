class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [1] * n
        for i in range(n):
            bits = 0
            while n:
                bits += 1
                n &= n - 1
            arr.append(bits)
        return arr