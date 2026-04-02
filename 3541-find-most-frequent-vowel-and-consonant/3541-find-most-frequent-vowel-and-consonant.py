class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        
        freq = {}
    
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        max_vowel = 0
        max_consonant = 0
        for ch in freq:
            if ch in vowels:
                if freq[ch] > max_vowel:
                    max_vowel = freq[ch]
            else:
                if freq[ch] > max_consonant:
                    max_consonant = freq[ch]
        
        return max_vowel + max_consonant