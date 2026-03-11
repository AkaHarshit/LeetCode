class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        lst = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(lst[-1]):
                lst.append(words[i])
        return lst