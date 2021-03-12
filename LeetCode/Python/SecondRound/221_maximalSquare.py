def maximalSquare(self, matrix: List[List[str]]) -> int:

    rows = len(matrix)
    cols = len(matrix[0])

    cache = dict()

    self.calculate(0, 0, rows, cols, matrix, cache)

    return max(cache.values()) ** 2


def calculate(self, r, c, rows, cols, matrix, cache):
    if r >= rows or c >= cols:
        return 0
    
    if (r, c) not in cache:
        down = self.calculate(r + 1, c, rows, cols, matrix, cache)
        right = self.calculate(r, c + 1, rows, cols, matrix, cache)
        diagonal = self.calculate(r + 1, c + 1, rows, cols, matrix, cache)

        cache[(r, c)] = 0
        if matrix[r][c] == "1":
            cache[(r, c)] = 1 + min(down, right, diagonal)
        
    return cache[(r, c)]