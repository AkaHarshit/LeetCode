class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
    
        matrix = []
        for i in range(rows):
            row = list(encodedText[i * cols:(i + 1) * cols])
            matrix.append(row)
    
        result = []
        for start_col in range(cols):
            i, j = 0, start_col
            while i < rows and j < cols:
                result.append(matrix[i][j])
                i += 1
                j += 1
        
        return "".join(result).rstrip()