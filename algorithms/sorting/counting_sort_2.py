import sys

n = int(input().strip())
array = [0] * n

numbers = [int(a) for a in input().strip().split(' ')]

# counts the numbers
for k in numbers:
    array[k] += 1

for i in range(n): # for each number from 0 to 99
    for j in range(array[i]): # if the number i was counted X times, print it X times
        sys.stdout.write(str(i) + ' ')