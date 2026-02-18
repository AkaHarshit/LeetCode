class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v = "aeiou"
        
        for i in s:
            if i in v:
                return True   
        
        return False          
