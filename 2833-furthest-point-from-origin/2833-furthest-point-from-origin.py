class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=moves.count('L')
        r=moves.count('R')
        b=moves.count('_')
        return abs(r-l)+b