class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(numbers):
            seen[num] = idx
        
        for idx, num in enumerate(numbers):
            needed = target - num
            if needed in seen:
                return [idx + 1, seen[needed] + 1]  
            

        