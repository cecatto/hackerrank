#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = 0
negative = 0
zeroes = 0
for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zeroes += 1

print('%.6f' % (positive / n))
print('%.6f' % (negative / n))
print('%.6f' % (zeroes / n))