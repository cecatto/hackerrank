#!/bin/python3

def isValid(s):
    m = {}

    for c in s:
        if m.get(c):
            m[c] += 1
        else:
            m[c] = 1

    values = list(m.values())
    last_count = values[0]
    changed = False

    for v in values:

        if v != last_count:
            if changed:
                if last_count != v:
                    return "NO"

            changed = True

            if v - 1 != 0 and abs(v - last_count) > 1:
                return "NO"

        else:
            last_count = v

    return "YES"


while True:
    s = input().strip()
    result = isValid(s)
    print(result)
