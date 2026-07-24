class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.quick_sort(nums)
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                if current_sum < 0:
                    left += 1
                if current_sum > 0:
                    right -= 1
    
        return result


            

    


    def quick_sort(self, nums:List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums)//2]
        left = []
        middle = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return self.quick_sort(left) + middle + self.quick_sort(right)
        