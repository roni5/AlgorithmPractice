def reArrange(lst):
  negativeIdx = 0
  for i in range(len(lst)):
    if lst[i] < 0:
      temp = lst[i]
      lst[i] = lst[negativeIdx]
      lst[negativeIdx] = temp
      negativeIdx += 1
  return lst
