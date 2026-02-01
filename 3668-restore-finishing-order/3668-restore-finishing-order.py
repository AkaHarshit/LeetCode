class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f_s = set(friends)
        lst = []
        
        for i in order:
            if i in f_s:
                lst.append(i)
        
        return lst
