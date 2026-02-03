from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        lst = [0] * n

        c = 0
        s = 0
        for i in range(n):
            lst[i] += s
            if boxes[i] == '1':
                c += 1
            s += c

        c = 0
        s = 0
        for i in range(n - 1, -1, -1):
            lst[i] += s
            if boxes[i] == '1':
                c += 1
            s += c

        return lst
