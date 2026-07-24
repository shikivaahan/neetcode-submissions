class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = 0
        k_min = 1
        for pile in piles:
            k_max = pile if pile > k_max else k_max

        minimum = k_max
        while k_min <= k_max:
            total = 0
            k = (k_min + k_max) // 2

            for pile in piles:
                total += -(-pile // k)
                
            if total > h:
                k_min = k + 1
            else:
                k_max = k - 1
                minimum = k if k < minimum else minimum

        return minimum 




            

        