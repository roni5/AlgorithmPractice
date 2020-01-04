#BFS

import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        q = collections.deque();
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append(Orange(i, j, 0));
    
        res = 0
        
        while q:
            
            orange = q.popleft()
            res = max(res, orange.layer)
            
            if (self.isInside(orange.x, orange.y - 1, row, col) and grid[orange.x][orange.y - 1] == 1):
                    q.append(Orange(orange.x, orange.y - 1, orange.layer + 1))
                    grid[orange.x][orange.y - 1] = 2
            if (self.isInside(orange.x, orange.y + 1, row, col) and grid[orange.x][orange.y + 1] == 1):
                    q.append(Orange(orange.x, orange.y + 1, orange.layer + 1))
                    grid[orange.x][orange.y + 1] = 2
            if (self.isInside(orange.x - 1, orange.y, row, col) and grid[orange.x - 1][orange.y] == 1):
                    q.append(Orange(orange.x - 1, orange.y, orange.layer + 1))
                    grid[orange.x - 1][orange.y] = 2
            if (self.isInside(orange.x + 1, orange.y, row, col) and grid[orange.x + 1][orange.y] == 1):
                    q.append(Orange(orange.x + 1, orange.y, orange.layer + 1))
                    grid[orange.x + 1][orange.y] = 2
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        
        return res
    
    def isInside(self,i,j,row,col):
        if i < 0 or i >= row or j < 0 or j >= col:
            return False
        return True
            
class Orange(object):
    def __init__(self, x, y, layer):
        self.x = x
        self.y = y
        self.layer = layer
    