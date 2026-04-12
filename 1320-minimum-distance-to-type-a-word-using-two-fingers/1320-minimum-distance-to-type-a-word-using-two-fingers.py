class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:
                return 0
            x1, y1 = a // 6, a % 6
            x2, y2 = b // 6, b % 6
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        memo = {}

        def dfs(i, f1, f2):
            if i == n:
                return 0

            if (i, f1, f2) in memo:
                return memo[(i, f1, f2)]

            curr = ord(word[i]) - ord('A')

            cost1 = dist(f1, curr) + dfs(i + 1, curr, f2)
            cost2 = dist(f2, curr) + dfs(i + 1, f1, curr)

            memo[(i, f1, f2)] = min(cost1, cost2)
            return memo[(i, f1, f2)]

        return dfs(0, -1, -1)