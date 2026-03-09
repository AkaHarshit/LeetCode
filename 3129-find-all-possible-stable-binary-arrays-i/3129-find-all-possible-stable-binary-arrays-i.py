class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]  
        dp1 = [[0]*(one+1) for _ in range(zero+1)] 
        
        for i in range(1, min(limit, zero)+1):
            dp0[i][0] = 1
            
        for j in range(1, min(limit, one)+1):
            dp1[0][j] = 1
        
        for z in range(zero+1):
            for o in range(one+1):
                
                if dp0[z][o] > 0:
                    for k in range(1, limit+1):
                        if o+k > one:
                            break
                        dp1[z][o+k] = (dp1[z][o+k] + dp0[z][o]) % MOD
                
                if dp1[z][o] > 0:
                    for k in range(1, limit+1):
                        if z+k > zero:
                            break
                        dp0[z+k][o] = (dp0[z+k][o] + dp1[z][o]) % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD