#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    result = 0

    for n in ar:
        result += n

    return result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
