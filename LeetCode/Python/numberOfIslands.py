 def numIslands(self, grid: List[List[str]]) -> int:

     island_num = 0

     if grid is None or len(grid == 0):
         return island_num
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == '1'):
                island_num += 1
                DFS(grid, i, j)
    
    return island_num

def DFS(grid, i, j):

    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
        return

    grid[i][j] = '0'
    DFS(grid, i - 1, j)
    DFS(grid, i + 1, j)
    DFS(grid, i , j - 1)
    DFS(grid, i , j + 1)