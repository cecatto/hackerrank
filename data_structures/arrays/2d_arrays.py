#!/bin/python3

import sys

n = 6
m = []
for arr_i in range(n):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   m.append(arr_t)

max_sum = -63

for i in range(n-2):
    for j in range(n-2):
        cur_sum = 0
        cur_sum += m[i][j]
        cur_sum += m[i][j+1]
        cur_sum += m[i][j+2]
        cur_sum += m[i+1][j+1]
        cur_sum += m[i+2][j]
        cur_sum += m[i+2][j+1]
        cur_sum += m[i+2][j+2]

        if cur_sum > max_sum:
            max_sum = cur_sum

print(max_sum)
