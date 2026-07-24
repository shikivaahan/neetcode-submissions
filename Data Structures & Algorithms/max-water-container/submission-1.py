class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            if heights[i] < heights[j]:
                amt = (j - i)*heights[i]
                i += 1
            else:
                amt = (j - i)*heights[j]
                j -= 1
            if max_amt < amt:
                max_amt = amt
            
        return max_amt
            



        