n, d = map(int, input().strip().split(' '))
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

res = arr[d:] + arr[:d]
#TODO: solve it using "in place" rotation

print(' '.join(map(str, res)))