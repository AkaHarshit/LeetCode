class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        lst = []
        c = 0
        for i in s:
            if i == '(':
                if c > 0:
                    lst.append(i)
                c += 1
            else:  
                c -= 1
                if c > 0:
                    lst.append(i)
        return "".join(lst)