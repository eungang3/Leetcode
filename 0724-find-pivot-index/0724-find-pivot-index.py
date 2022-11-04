class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        
        for index, current in enumerate(nums):
            if left == (total - current - left):
                return index
            left += current
            
        return -1