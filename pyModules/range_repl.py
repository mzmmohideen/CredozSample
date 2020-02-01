def range(*n):
    start = 0
    step = 1
    l = []
    if len(n) == 1:
      stop = n[0]
    elif len(n) == 2:
      start, stop = n
    elif len(n) == 3:
      start, stop, step = n
    else:
      return "Invalid Input"

    while start < stop:
        l.append(start)
        start+=step
    return l



print range(1, 10, 2)