class Solution:
    def mirrorDistance(self, n: int) -> int:
        o = n
        c = 0
        while n > 0:
            d = n % 10
            c = c * 10 + d
            n //= 10
        return abs(o - c)