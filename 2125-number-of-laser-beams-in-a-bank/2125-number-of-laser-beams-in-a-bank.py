class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        p = 0
        c = 0
        for i in bank:
            ans = i.count('1')
            if ans > 0:
                c += p * ans
                p = ans
        return c