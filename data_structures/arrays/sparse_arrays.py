n = int(input().strip())
lines = dict()

for i in range(n):
    line = input().strip()
    if not lines.get(line):
        lines[line] = 1
    else:
        lines[line] += 1

q = int(input().strip())

for i in range(q):
    query = input().strip()
    print(lines.get(query, 0))
