class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        lst = []
        c = ['a', 'b', 'c']
        def backtrack(curr):
            if len(curr) == n:
                lst.append(curr)
                return
            for i in c:
                if not curr or curr[-1] != i:
                    backtrack(curr + i)
        backtrack("")
        if k <= len(lst):
            return lst[k-1]
        return ""