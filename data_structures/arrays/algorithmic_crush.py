n, m = map(int, input().strip().split(' '))
# values = [0 for i in range(n)]
diff_array = [0 for i in range(n+1)]
max_sum = 0

for _ in range(m):
    a, b, k = map(int, input().strip().split(' '))

    # O(MN)
    # for j in range(a-1, b):
    #     values[j] += k
    #     if values[j] > max_sum:
    #         max_sum = vallues[j]

    diff_array[a-1] += k
    diff_array[b] -= k

prefix_sum = 0
for i in range(n):
    prefix_sum += diff_array[i]
    if prefix_sum > max_sum:
        max_sum = prefix_sum

print(max_sum)

