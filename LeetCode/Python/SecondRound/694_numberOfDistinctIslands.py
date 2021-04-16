def numDistinctIslands(self, grid: List[List[int]]) -> int:

    if not grid or len(grid) == 0:
        return 0

    islands = set()
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                path = self.computePath(grid, row, col, rows, cols, "X")
                islands.add(path)
    
    return len(islands)

def computePath(self, grid, row, col, rows, cols, direction):

    if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
        return "O"
    
    grid[row][col] = 0
    left = self.computePath(grid,row, col - 1, rows, cols, "L")
    right = self.computePath(grid,row, col + 1, rows, cols, "R")
    up = self.computePath(grid,row - 1, col, rows, cols, "U")
    down = self.computePath(grid,row + 1, col, rows, cols, "D")

    return direction + left + right + up + down