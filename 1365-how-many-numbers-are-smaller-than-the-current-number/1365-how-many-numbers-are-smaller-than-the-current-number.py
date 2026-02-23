class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = [0] * 101   
        for i in nums:
            c[i] += 1
        for i in range(1, 101):
            c[i] += c[i-1]
        lst = []
        for i in nums:
            if i == 0:
                lst.append(0)
            else:
                lst.append(c[i-1])
        return lst