class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        c = 0
        for i in left:
            if i > c:
                c = i
        for i in right:
            if n - i > c:
                c = n - i
        return c