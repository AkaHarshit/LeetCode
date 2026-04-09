class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        lst = []
        for i in people:
            lst.insert(i[1], i)
        
        return lst 