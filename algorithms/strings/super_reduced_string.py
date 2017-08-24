#!/bin/python3

def super_reduced_string(s):
    i = 1

    while i < len(s):
        if s[i-1] == s[i]:
            s = s[0:i-1] + s[i+1:]
            if i > 1:
                i -= 1
        else:
            i += 1

    return s or "Empty String"


s = input().strip()
result = super_reduced_string(s)
print(result)
