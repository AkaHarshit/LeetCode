class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        lst = []
        for i in points:
            lst.append(i[0])
        lst.sort()
        c = 0
        for i in range(1, len(lst)):
            g = lst[i] - lst[i - 1]
            if g > c:
                c = g
        return c