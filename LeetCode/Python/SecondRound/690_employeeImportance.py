def getImportance(self, employees: List['Employee'], id: int) -> int:

    map = defaultdict()
    for employee in employees:
        map[employee.id] = employee
    
    queue = deque()
    queue.append(id)
    importance = 0

    while queue:
        employee = map[queue.popleft()]
        importance += employee.importance
        for sub in employee.subordinates:
            queue.append(sub)
    
    return importance