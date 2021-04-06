def countComponents(self, n: int, edges: List[List[int]]) -> int:

    adjList = self.getAdjList(edges)
    visited = set()
    components = 0

    for i in range(n):
        if i not in visited:
            components += 1
            self.dfs(i, visited, adjList)

    return components

def dfs(self, node, visited, adjList):
    
    visited.add(node)
    for point in adjList[node]:
        if point not in visited:
            self.dfs(point, visited, adjList)


def getAdjList(self, edges, n):

    adjList = defaultdict(list)

    for i in range(len(edges)):
        adjList[edges[i][0]].append(edges[i][1])
        adjList[edges[i][1]].append(edges[i][0])

    return adjList 