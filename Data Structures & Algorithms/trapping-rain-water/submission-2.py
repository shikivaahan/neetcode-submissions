class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = len(height) - 1
        left_wall = 0
        right_wall = 0

        while left < right:
            if height[left] < height[right]:
                left_wall = max(left_wall, height[left])
                total += left_wall - height[left]
                left += 1
            else:
                right_wall = max(right_wall, height[right])
                total += right_wall - height[right]
                right -= 1
            
        return total
                
                
             
        