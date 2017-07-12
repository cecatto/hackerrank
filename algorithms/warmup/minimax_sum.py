#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()

sum_arr = 0
for n in arr:
    sum_arr += n

sum_min = sum_arr - arr[-1]
sum_max = sum_arr - arr[0]

print('%d %d' %(sum_min, sum_max))