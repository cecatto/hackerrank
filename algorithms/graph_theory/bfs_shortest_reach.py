#!/bin/python3

import sys


def bfs(graph, start):
    visited = set()
    queue = [start]
    level = [0]
    path = {}

    while queue:
        node = queue.pop(0)
        current_level = level.pop(0)

        if node not in visited:
            visited.add(node)
            children = graph[node] - visited
            children_level = current_level + 1
            queue.extend(children)
            for i in children:
                if not path.get(i):
                    path[i] = children_level
                level.append(children_level)

    return path

# MAIN
q = int(input().strip())
for a0 in range(q):
    graph = {}
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]

    for a1 in range(m):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]

        if not graph.get(u): graph[u] = set()
        if not graph.get(v): graph[v] = set()

        graph[u].add(v)
        graph[v].add(u)

    s = int(input().strip())

    result = bfs(graph, s)

    nodes = set(graph.keys())
    visited = set(result.keys())
    visited.add(s)
    sorted_visited = sorted(visited)

    for i in range(1, n+1):
        if i == s:
            continue
        if i in sorted_visited:
            sys.stdout.write(str(result[i] * 6))
        else:
            sys.stdout.write(str(-1))

        sys.stdout.write(' ')

    sys.stdout.write('\n')
