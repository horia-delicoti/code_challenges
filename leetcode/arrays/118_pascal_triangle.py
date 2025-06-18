# Given an integer numRows, return the first numRows of Pascal's triangle.

# numsRows = 5
# output = [1, [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def generate(numRows):
    if numRows <= 0:
        return []
    
    triangle = []
    for row in range(numRows):
        # Start each row with 1
        current_row = [1] * (row + 1)
        # Fill in the values for the current row based on the previous row
        for j in range(1, row):
            current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        # Append the current row to the triangle
        triangle.append(current_row)
    return triangle

numRows = 5
output = generate(numRows)
print(output)  # Expected output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]