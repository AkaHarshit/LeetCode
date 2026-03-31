class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def solve(expr):
            res = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            if not res:
                res.append(int(expr))
            
            return res
        
        return solve(expression)