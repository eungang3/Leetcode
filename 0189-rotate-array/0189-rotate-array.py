class Solution:
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            nums[li], nums[ri] = nums[ri], nums[li]
            
            li += 1
            ri -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);