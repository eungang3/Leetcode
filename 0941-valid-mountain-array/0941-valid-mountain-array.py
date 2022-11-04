class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        left = 0
        right = len(arr) - 1
        
        while left < len(arr) - 2 and arr[left] < arr[left + 1]:
            left += 1
        
        while 1 < right and arr[right] < arr[right - 1]:
            right -= 1
            
        return left == right