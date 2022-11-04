class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[val_index] = nums[val_index], nums[i]
                val_index += 1
            
        return val_index