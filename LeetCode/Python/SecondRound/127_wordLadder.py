def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

    if endWord not in wordList:
        return 0
    
    graph = self.createGraph(wordList)
    queue = deque()
    queue.append((beginWord, 1))
    visited = set()

    while queue:
        curr, level = queue.popleft()
        for i in range(len(curr)):
            wildcard = curr[:i] + "*" + curr[i + 1:]
            if wildcard in graph:
                for word in graph[wildcard]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
    
    return 0


def createGraph(self, wordList):
    graph = dict()
    for word in wordList:
        for i in range(len(word)):
            wildcard = word[:i] + "*" word[i + 1:]
            if wildcard not in graph:
                graph[wildcard] = []
            graph[wildcard].append(word)