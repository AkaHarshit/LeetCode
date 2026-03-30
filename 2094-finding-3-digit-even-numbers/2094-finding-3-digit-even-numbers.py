class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        
        res = []
        for num in range(100, 1000):
            if num % 2 != 0:
                continue
            
            a = num // 100
            b = (num // 10) % 10
            c = num % 10
            
            temp = freq.copy()
            
            if temp[a] > 0:
                temp[a] -= 1
            else:
                continue
            
            if temp[b] > 0:
                temp[b] -= 1
            else:
                continue
            
            if temp[c] > 0:
                temp[c] -= 1
            else:
                continue
            
            res.append(num)
        
        return res