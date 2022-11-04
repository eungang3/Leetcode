class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ref = set()
        
        for num in arr:
            if num * 2 in ref or num / 2 in ref:
                return True
            ref.add(num)
        
        return False