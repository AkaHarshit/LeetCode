class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = ""
        for i in range(n):
            if nums[i][i]=='0':
                s+='1'
            else:
                s+='0'
        return s