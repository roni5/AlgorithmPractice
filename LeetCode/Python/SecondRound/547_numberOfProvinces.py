def findCircleNum(self, isConnected: List[List[int]]) -> int:

    provinces = 0
    visited = set()
    for city in range(len(isConnected)):
        if city not in visited:
            provinces += 1
            self.dfs(city, isConnected, visited)

    return provinces

def dfs(self, city, isConnected, visited):
    
    visited.add(city)
    for neighbor in range(len(isConnected[city])):
        if isConnected[city][neighbor] == 1 and neighbor not in visited:
            self.dfs(neighbor, isConnected, visited)
