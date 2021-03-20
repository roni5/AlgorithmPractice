def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    maxArea = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                maxArea = max(maxArea, self.area(row, col, grid, rows, cols))
    
    return maxArea


def area(self, row, col, grid, rows, cols):

    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
        return 0
    
    grid[row][col] = 0
    left = self.area(row, col - 1, grid, rows, cols)
    right = self.area(row, col + 1, grid, rows, cols)
    up = self.area(row - 1, col, grid, rows, cols)
    down = self.area(row + 1, col, grid, rows, cols)

    return 1 + left + right + up + down
    