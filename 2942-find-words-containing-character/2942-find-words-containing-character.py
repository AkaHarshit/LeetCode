class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst = []
        
        for i in range(len(words)):
            if x in words[i]:
                lst.append(i)
                
        return lst