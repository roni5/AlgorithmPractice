def compress(chars):
    read = write = 0

    while read < len(chars):
        
        count = 1
        nxt = read + 1
        while nxt < len(chars) and chars[read] == chars[nxt]:
            count += 1
            nxt += 1
        
        chars[write] = chars[read]
        write += 1
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1
        read = nxt
    
    return write