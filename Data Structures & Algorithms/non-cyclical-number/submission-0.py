class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            n = (n / 10) + (n % 10) ** 2
        return n == 1
        

        