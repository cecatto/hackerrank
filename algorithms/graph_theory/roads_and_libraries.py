#!/bin/python3

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


# main
q = int(input().strip())

for a0 in range(q):
    graph = {}
    n, m, c_lib, c_road = map(int, input().strip().split(' '))

    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')

        if not graph.get(city_1): graph[city_1] = set()
        if not graph.get(city_2): graph[city_2] = set()

        graph[city_1].add(city_2)
        graph[city_2].add(city_1)

    if c_lib <= c_road:
        print(n * c_lib)
        continue

    cities = set(graph.keys())
    cost = 0
    visited = set()
    non_visited =  cities - visited

    while non_visited:
        component = dfs(graph, non_visited.pop())
        cost += (len(component) - 1) * c_road + c_lib
        visited |= component
        non_visited = cities - visited

    print(cost)