class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if heights[i] <= heights[j]:
                    amount = (j - i)*heights[i]
                else:
                    amount = (j - i)*heights[j]
                if amount > max_amt:
                    max_amt = amount
                else:
                    continue
        return max_amt



        