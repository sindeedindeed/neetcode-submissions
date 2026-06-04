class Solution:
    def climbStairs(self, n: int) -> int:
        var1, var2 = 0, 0
        for i in range(1, n - 1):
            temp = var1
            var1 = var1+var2
            var2 = temp
        return var1