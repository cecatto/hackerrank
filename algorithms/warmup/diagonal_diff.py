#!/bin/python3

import sys


n = int(input().strip())
m = []

for a_i in range(n):
    a_t = [int(m_temp) for m_temp in input().strip().split(' ')]
    m.append(a_t)

d1 = 0
d2 = 0
for i in range(n):
    d1 += m[i][i]
    d2 += m[n-1 - i][i]

print(abs(d1 - d2))