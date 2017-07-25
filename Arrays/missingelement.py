def finder(arr1, arr2):
    seen = {}

    for num in arr1:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    for num in arr2:
        if num in seen:
            seen[num] -= 1

    for num in seen:
        if seen[num] != 0:
            missing = num

    print("Missing elemnts are " + str(missing))

finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])