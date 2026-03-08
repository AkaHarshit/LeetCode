class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        c = 0
        for i in range(num1, num2 + 1):
            s = str(i)
            n = len(s)
            if n < 3:
                continue
            w = 0
            for i in range(1, n - 1):
                if (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):
                    w+=1
            c+=w
        return c