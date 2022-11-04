class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            current = abs(nums[i]) - 1
            if nums[current] > 0:
                nums[current] *= -1
            
        result = []
        
        for index, value in enumerate(nums):
            if value > 0:
                result.append(index + 1)
                
        return result