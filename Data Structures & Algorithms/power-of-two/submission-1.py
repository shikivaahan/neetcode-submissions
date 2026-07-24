class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n < 1:
            return False

        i = 0
        while n % 2 == 0:
            n = n / 2
        
        return n == 1
        