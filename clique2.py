# When adding an interval, the right border should have +1

arr = [list(range(0, 21)),
       list(range(0, 15)),
       list(range(0, 8)),
       list(range(1, 4)),
       list(range(1, 6)),
       list(range(3, 6)),
       list(range(5, 7))]

boards = []  # new intervals
for i in arr:
    boards.append(list(i)[0])
    boards.append(list(i)[len(i)-1])
boards = list(set(boards))

eps = 0.01
for i in range(len(arr)):
    arr[i][0], arr[i][len(arr[i])-1] = arr[i][0] + eps, arr[i][len(arr[i])-1] - eps
    arr[i] = set(arr[i])

timed = []  # new intervals with the number of intersections
for i in range(len(boards)-1):
    curr = [set(range(boards[i], boards[i+1]+1)), 0]  # [{new interval}, number of intersections on it]
    for j in arr:
        if curr[0].intersection(j):
            curr[1] += 1
    timed.append(curr)

maxim = [0, 0]  # 1st - max amount of intersections, 2nd - index of best interval
for i in range(len(timed)):
    if timed[i][1] > maxim[0]:
        maxim = [timed[i][1], i]
array_for_answer = []
for i in arr:
    a = timed[maxim[1]][0].intersection(i)
    if a:
        i = list(i)
        i.sort()
        i[0], i[len(i)-1] = round(i[0] - eps), round(i[len(i)-1] + eps)
        array_for_answer.append(i)
for i in array_for_answer:
    print(i)
