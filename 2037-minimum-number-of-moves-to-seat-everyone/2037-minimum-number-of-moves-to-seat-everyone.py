class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        c = 0
        for i in range(len(seats)):
            if seats[i] > students[i]:
                c += seats[i] - students[i]
            else:
                c += students[i] - seats[i]
        return c