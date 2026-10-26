def dls(graph, node, goal, limit, path):
    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(
                graph, neighbor, goal,
                limit - 1, path + [neighbor]
            )

            if result is not None:
                return result

    return None


def iddfs(graph, start, goal):
    for depth in range(len(graph) + 1):
        print("Searching at depth:", depth)

        result = dls(graph, start, goal, depth, [start])

        if result is not None:
            print("Goal found!")
            print("Path:", " -> ".join(result))
            print("Depth:", len(result) - 1)
            return

    print("No path found")


graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v = input("Enter edge (source destination): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, [])

start = input("Enter start node: ")
goal = input("Enter goal node: ")

graph.setdefault(start, [])
graph.setdefault(goal, [])

iddfs(graph, start, goal)
