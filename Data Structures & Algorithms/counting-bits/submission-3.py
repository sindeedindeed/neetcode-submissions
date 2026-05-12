class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            result = 0
            for j in range(i):
                result <<= 1 | (i & 1)
            arr.append(result)

        return arr


