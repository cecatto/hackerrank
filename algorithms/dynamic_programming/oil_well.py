#!/bin/python3
# fails

r, c = map(int, input().strip().split(' '))
m = []

for i in range(r):
    row = [int(n) for n in input().strip().split(' ')]
    m.append(row)


def distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def permute(arr, low=0):
    if low + 1 >= len(arr):
        yield arr
    else:
        for p in permute(arr, low + 1):
            yield p
        for i in range(low + 1, len(arr)):
            arr[low], arr[i] = arr[i], arr[low]
            for p in permute(arr, low + 1):
                yield p
            arr[low], arr[i] = arr[i], arr[low]

wells = []

for x in range(r):
    for y in range(c):
        if m[x][y] == 1:
            wells.append((x + 1, y + 1))

min_cost = float("inf")

for p in permute(wells):
    cost = 0
    for i in range(1, len(wells)):
        cost += distance(wells[i-1], wells[i])

    if cost < min_cost:
        min_cost = cost

print(min_cost)