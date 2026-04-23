class Solution:
    def minimumSum(self, num: int) -> int:
        d1 = num % 10
        num //= 10
        d2 = num % 10
        num //= 10
        d3 = num % 10
        num //= 10
        d4 = num % 10
        digits = [d1, d2, d3, d4]
        digits.sort()
        new1 = digits[0] * 10 + digits[2]
        new2 = digits[1] * 10 + digits[3]
        
        return new1 + new2