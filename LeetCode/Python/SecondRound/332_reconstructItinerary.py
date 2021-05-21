import collections
def findItinerary(self, tickets: List[List[str]]) -> List[str]:

    graph = collections.defaultdict(list)

    for org, dest in sorted(tickets):
        graph[org].append(dest)
    
    route = []
    self.dfs(route, graph, "JFK")

    return route[::-1]

def dfs(self, route, graph, org):

    while graph[org]:
        self.dfs(route, graph, graph[org].pop(0))
    route.append(org)
