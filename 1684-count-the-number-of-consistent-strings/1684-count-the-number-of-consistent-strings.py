class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)  
        c = 0
        for i in words:
            is_c = True
            for i in i:
                if i not in s:
                    is_c = False
                    break
            if is_c:
                c += 1
        return c