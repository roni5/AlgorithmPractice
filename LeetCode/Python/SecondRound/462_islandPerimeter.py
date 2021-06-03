def islandPerimeter(self, grid: List[List[int]]) -> int:

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += self.dfs(grid, row, col)

    return perimeter

def dfs(self, grid, row, col):
    if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == 0:
        return 1
    
    if grid[row][col] == -1:
        return 0
    
    grid[row][col] = -1
    perim = self.dfs(grid, row, col + 1)
    perim += self.dfs(grid, row, col -1)
    perim += self.dfs(grid, row + 1, col)
    perim += self.dfs(grid, row -1, col)

    return perim