class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        c = 0
        for i in garbage:
            c += len(i)
        m = 0
        p = 0
        g = 0
        
        for i in range(n):
            if 'M' in garbage[i]:
                m = i
            if 'P' in garbage[i]:
                p = i
            if 'G' in garbage[i]:
                g = i

        t = c
        
        for i in range(m):
            t += travel[i]
        
        for i in range(p):
            t += travel[i]
        
        for i in range(g):
            t += travel[i]
        
        return t