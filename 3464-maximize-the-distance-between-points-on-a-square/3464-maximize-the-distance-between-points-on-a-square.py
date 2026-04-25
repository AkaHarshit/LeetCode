class Solution:
    def maxDistance(self, side, points, k):
        
        def getPos(x, y):
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y
        
        arr = sorted(getPos(x, y) for x, y in points)
        n = len(arr)
        per = 4 * side
        
        arr2 = arr + [x + per for x in arr]
        def lower_bound(a, target, l, r):
            while l < r:
                mid = (l + r) // 2
                if a[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def can(d):
            for i in range(n):
                count = 1
                last = arr2[i]
                pos = i
                
                for _ in range(k - 1):
                    nxt = lower_bound(arr2, last + d, pos + 1, i + n)
                    if nxt == i + n:
                        break
                    count += 1
                    last = arr2[nxt]
                    pos = nxt
                
                if count == k and arr2[i] + per - last >= d:
                    return True
            
            return False
        
        low, high = 0, per
        
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high