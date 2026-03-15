class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        lst = []
        for i in queries:
            x = i[0]
            y = i[1]
            r = i[2]
            r2 = r * r
            
            c = 0
            
            for i in points:
                dx = i[0] - x
                dy = i[1] - y
                if dx * dx + dy * dy <= r2:
                    c += 1
            lst.append(c)
        return lst