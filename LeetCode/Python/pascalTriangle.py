def generate(self, num_rows):
    triangle = []

    for nth_row in range(num_rows):
        row = [None for x in range(nth_row + 1)]
        row[0], row[-1] = 1, 1

        if nth_row > 1:
            for i in range(len(row) - 1):
                row[i] = triangle[nth_row - 1][i - 1] + triangle[nth_row - 1][i]
        triangle.append(row)
    
    return triangle