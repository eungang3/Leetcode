class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxValue = max(nums)
        maxIndex = nums.index(maxValue)
        
        for num in nums:
            if num != maxValue and maxValue < num * 2:
                return -1
        
        return maxIndex