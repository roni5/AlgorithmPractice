def closedIsland(self, grid: List[List[int]]) -> int:

    if not grid or len(grid) == 0:
        return 0
    
    islands = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == 0:
                if self.isClosedIsland(grid, row, col, rows, cols):
                    islands += 1
    
    return islands

def isClosedIsland(self, grid, row, col, rows, cols):
    
    # 1 water
    # 0 land
    if grid[row][col] == 1:
        return True
    if self.isOnPerimeter(row, col, rows, cols):
        return False
    
    grid[row][col] = 1
    
    left = self.isClosedIsland(grid, row, col - 1, rows, cols)
    right = self.isClosedIsland(grid, row, col + 1, rows, cols)
    up = self.isClosedIsland(grid, row - 1, col, rows, cols)
    down = self.isClosedIsland(grid, row + 1, col, rows, cols)
    
    return left and right and up and down

def isOnPerimeter(self, row, col, rows, cols):
    return row == 0 or col == 0 or row == rows - 1 or col == cols - 1