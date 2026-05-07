class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                arr[i] = 0
            arr[i] = arr[i >> 1] + (i & 1)
        return arr


