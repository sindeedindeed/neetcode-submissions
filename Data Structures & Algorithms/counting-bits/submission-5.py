class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            count = 0
            copy = i
            while copy > 0:
                count += copy & 1
                copy >>= 1
            arr.append(count)
        return arr


