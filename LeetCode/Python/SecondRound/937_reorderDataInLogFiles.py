


def reorderLogFiles(logs):
    
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        if log.split(" ")[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)
        
    letter_logs.sort(key = lambda x: x.split(" ")[0])
    letter_logs.sort(key = lambda x: x.split(" ")[1:])
    result = letter_logs + digit_logs
    return result