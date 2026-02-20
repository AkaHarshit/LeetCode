class Solution:
    def validStrings(self, n: int) -> List[str]:
        lst = []

        def helper(c):
            if len(c)==n:
                lst.append(c)
                return
            helper(c + "1")
            if len(c)==0 or c[-1]!="0":
                helper(c+"0")
        helper("")
        return lst