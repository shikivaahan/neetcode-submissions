class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []

        for right in range(k - 1, len(nums)):
            left = right - k + 1
            maximum = max(nums[left:right + 1])
            maximums.append(maximum)
        
        return maximums


        