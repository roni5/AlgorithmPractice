def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

    if grid[0][0] == 1:
        return - 1
    
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    queue.append((0, 0, 1))
    grid[0][0] = 1

    directions = [(0,1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while queue:
        size = len(queue)
        for i in range(size):
            x, y, step = queue.popleft()
            if x == rows - 1 and y == cols - 1:
                return step
            for direction in directions:
                row = x + direction[0]
                col = y + direction[1]
                if row >= 0 and col >= 0 and row < rows and col < cols and grid[0][0] == 0:
                    queue.append((row, col, step + 1))
                    grid[row][col] = 1

    return -1