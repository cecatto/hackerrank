#!/bin/python3

import sys

def timeConversion(input):
    # Complete this function
    am = input[-2:] == 'AM'
    h, m, s = map(int, input[0:-2].split(':'))

    if not am and h != 12:
        h += 12
    elif am and h == 12:
        h = 0

    return '%02d:%02d:%02d' % (h, m, s)

s = input().strip()
result = timeConversion(s)
print(result)
