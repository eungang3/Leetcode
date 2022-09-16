class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(str(digit) for digit in digits))
        return list(str(number + 1))