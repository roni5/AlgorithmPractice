import collections
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)

    for course, pre in prerequisites:
        graph[course].append(pre)
    
    visited = set()

    for course in range(numCourses):
        if not self.dfs(graph, visited, course):
            return False
    
    return True


def dfs(self, graph, visited, course):

    if course in visited:
        return False
    
    if len(graph[course]) == 0:
        return True
    
    visited.add(course)
    for pre in graph[course]:
        if not self.dfs(graph, visited, pre):
            return False
    
    visited.discard(course)
    graph[course] = []

    return True