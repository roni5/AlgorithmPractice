def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    graph = self.createGraph(prerequisites)

    visited = set()
    cycle = set()
    output = []

    for course in range(numCourses):
        if self.dfs(course, visited, cycle, output, graph) == False:
            return []

    return output

def createGraph(self, prerequisites):

    graph = defaultdict(list)
    
    for course, preq in prerequisites:
        graph[course].append(preq)
    
    return graph

def dfs(self, course, visited, cycle, output, graph):

    if course in cycle:
        return False
    
    if course in visited:
        return True
    
    cycle.add(course)
    for preq in graph[course]:
        if self.dfs(preq, visited, cycle, output, graph) == False:
            return False
    
    cycle.remove(course)
    visited.add(course)
    output.append(course)

    return True