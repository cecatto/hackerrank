#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    highest = 0
    count = 0

    for k in ar:
        if k > highest:
            highest = k
            count = 1
        elif k == highest:
            count += 1

    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
