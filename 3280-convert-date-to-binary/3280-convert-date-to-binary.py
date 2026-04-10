class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        y_bin = bin(int(year))[2:]
        m_bin = bin(int(month))[2:]
        d_bin = bin(int(day))[2:]
        return y_bin + '-' + m_bin + '-' + d_bin