def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1  # Set the first and last elements of the row to 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

# Example usage:
rows = 5
pascals_triangle = generate_pascals_triangle(rows)
for row in pascals_triangle:
    print(" ".join(map(str, row)))
