class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2  
        c = [0] * n
        lst = []
        for i in nums:
            c[i] += 1
        for i in range(n):
            if c[i] > 1:
                lst.append(i)
        return lst