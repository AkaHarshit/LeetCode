class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        for a, b in allowedSwaps:
            union(a, b)
        groups = {}
        for i in range(len(source)):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        mismatch = 0
        
        for indices in groups.values():
            freq = {}
            for i in indices:
                val = source[i]
                freq[val] = freq.get(val, 0) + 1
            for i in indices:
                val = target[i]
                if val in freq and freq[val] > 0:
                    freq[val] -= 1
                else:
                    mismatch += 1
        
        return mismatch