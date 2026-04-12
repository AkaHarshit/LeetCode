class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = [0] * 26
        for ch in letters:
            freq[ord(ch) - ord('a')] += 1

        n = len(words)
        word_freq = []
        word_score = []

        for word in words:
            f = [0] * 26
            s = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                f[idx] += 1
                s += score[idx]
            word_freq.append(f)
            word_score.append(s)
        def dfs(i, freq):
            if i == n:
                return 0
            max_score = dfs(i + 1, freq)
            can_take = True
            for j in range(26):
                if word_freq[i][j] > freq[j]:
                    can_take = False
                    break

            if can_take:
                for j in range(26):
                    freq[j] -= word_freq[i][j]
                max_score = max(max_score, word_score[i] + dfs(i + 1, freq))
                for j in range(26):
                    freq[j] += word_freq[i][j]

            return max_score

        return dfs(0, freq)