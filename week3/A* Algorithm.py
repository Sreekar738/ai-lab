import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    cost = {start: 0}
    parent = {start: None}

    while pq:
        f, g, node = heapq.heappop(pq)

        if g != cost.get(node):
            continue

        if node == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nPath found:")
            print(" -> ".join(path))
            print("Total cost:", g)
            print("\nPath steps:")

            for i, n in enumerate(path):
                print("Step", i, ":", n)

            return

        for neighbor, weight in graph.get(node, []):
            new_g = g + weight

            if new_g < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_g
                parent[neighbor] = node

                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    print("No path found")


graph = {}
heuristic = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v, w = input(
        "Enter edge (source destination cost): "
    ).split()

    graph.setdefault(u, []).append((v, float(w)))
    graph.setdefault(v, [])

nodes = set(graph)

for edges in graph.values():
    for neighbor, weight in edges:
        nodes.add(neighbor)

print("\nEnter heuristic values:")
for node in sorted(nodes):
    heuristic[node] = float(input(f"h({node}) = "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

if start not in graph or goal not in graph:
    print("Invalid start or goal node")
else:
    a_star(graph, heuristic, start, goal)
