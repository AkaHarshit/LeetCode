class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        lst = []
        for q in queries:
            for d in dictionary:
                c = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        c += 1
                        if c > 2:
                            break
                if c <= 2:
                    lst.append(q)
                    break  
        return lst