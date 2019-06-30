def findSecondMaximum(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    
    return second if second != float('inf') else None


print(findSecondMaximum([1, 2, 3, 6,7,3,4]))
