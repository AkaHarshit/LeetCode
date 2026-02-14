class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}      
        lst = []

        for i in range(len(groupSizes)):
            s = groupSizes[i]
            if s not in d:
                d[s] = []
            d[s].append(i)

            if len(d[s]) == s:
                lst.append(d[s])
                d[s] = []
        return lst