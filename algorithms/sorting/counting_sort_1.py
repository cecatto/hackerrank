import sys

n = int(input().strip())
array = [0 for i in range(100)]

numbers = [int(a) for a in input().strip().split(' ')]

for k in numbers:
    array[k] += 1

for k in array:
    sys.stdout.write(str(k) + ' ')