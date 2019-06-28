def chatRecord(records):
    answer = []
    events = []
    ids = {}
    for record in records:
        temp = record.split(" ")
        action = temp[0]
        id = temp[1]
        if(action == "Enter" or action =="Change"):
            ids[id] = temp[2]
        events.append((action, id))
    
    for event in events:
        nickName = ids[event[1]]
        if(event[0] == "Enter"):
            answer.append(f'{nickName}님이 들어왔습니다')
        elif(event[0] == "Leave"):
            answer.append(f'{nickName}님이 나갔습니다')
    
    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(chatRecord(records))
