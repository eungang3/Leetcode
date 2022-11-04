class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = maximum
            maximum = max(maximum, current)
            
        return arr