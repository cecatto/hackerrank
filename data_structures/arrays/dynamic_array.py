# fails

s = []
last_answer = 0
n, nq = map(int, input().strip().split(' '))
queries = []

for i in range(nq):
    queries.append([int(arr_temp) for arr_temp in input().strip().split(' ')])

for i in range(n):
    s.append([])

for q in queries:
    q_type = q[0]
    i = (q[1] ^ last_answer) % n
    y = q[2]

    if(q_type == 1):
        s[i].append(y)
    else:
        last_answer = s[i][y % len(s[i])]
        print(last_answer)
