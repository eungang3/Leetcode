class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_index = 0
        
        for i in range(len(nums)):
            # 짝수인 경우
            if nums[i] % 2 == 0:
                nums[odd_index], nums[i] = nums[i], nums[odd_index]
                odd_index += 1
                
        return nums