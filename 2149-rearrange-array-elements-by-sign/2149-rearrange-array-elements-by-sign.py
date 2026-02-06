class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for i in nums:
            if i > 0:
                p.append(i)
            else:
                n.append(i)
    
        lst = []
        for i in range(len(p)):
            lst.append(p[i])
            lst.append(n[i])
        return lst