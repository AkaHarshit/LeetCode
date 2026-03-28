class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        res = [''] * n
        ch = ord('a')

        for i in range(n):
            if res[i] != '':
                continue
            
            if ch > ord('z'):
                return ""
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = chr(ch)
            
            ch += 1
        
        word = "".join(res)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i == n-1 or j == n-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word