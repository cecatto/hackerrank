#!/bin/python3

import sys


def solve(a0, a1, a2, b0, b1, b2):
    # for arg in locals().items():
    #     if arg < 1 or arg > 100:
    #         raise ValueError('Invalid arg: ' + arg)

    alice = 0
    bob = 0

    def compare(a, b):
        nonlocal alice, bob

        if a > b:
            alice += 1
        elif b > a:
            bob += 1

    compare(a0, b0)
    compare(a1, b1)
    compare(a2, b2)

    return alice, bob


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
