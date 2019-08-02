def groupAnagram(strs):

    grouped = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(word)
    
    return list(grouped.values())