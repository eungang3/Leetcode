class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)

        for i in range(len(nums)):
            current = nums[i]
            right = total - current
            if left == right:
                return i
            left += current
            total = right
        return -1