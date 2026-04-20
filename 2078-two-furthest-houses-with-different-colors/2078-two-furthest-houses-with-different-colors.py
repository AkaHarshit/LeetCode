class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        c = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                c = max(c, i - 0)
                break
        for i in range(n):
            if colors[i] != colors[n - 1]:
                c = max(c, (n - 1) - i)
                break
        return c