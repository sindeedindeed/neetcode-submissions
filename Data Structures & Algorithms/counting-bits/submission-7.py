class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * n
        for i in range(n + 1):
            if i == 0:
                arr[i] = 0
            arr[i] = arr[i >> 1] + 1
        return arr


