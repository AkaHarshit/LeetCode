class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        lst = [0] * n
        if k == 0:
            return lst
        for i in range(n):
            s = 0
            if k > 0:
                for j in range(1, k + 1):
                    s += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    s += code[(i - j + n) % n]   
            lst[i] = s
        return lst