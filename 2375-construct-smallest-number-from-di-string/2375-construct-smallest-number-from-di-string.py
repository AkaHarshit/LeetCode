class Solution:
    def smallestNumber(self, pattern: str) -> str:
        lst = []
        s = ""
        n = len(pattern)
        for i in range(n + 1):
            lst.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while lst:
                    s += lst.pop()
        return s