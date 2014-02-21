import random
import time


def create_random_graph(nodes):
    """ Creates a random (directed) graph with the given number of nodes """
    graph = []

    for i in range(0, nodes):
        graph.append([])
        for j in range(0, nodes):
            rand = random.randint(1, 100)
            if rand % 2 == 0 and i != j:
                graph[i].append(rand)
            else:
                graph[i].append(-1)

    return graph


def shortest_path_simple(graph, start, end, path=[], length=0, steplength=0):
    """ Finds the shortest path in a weighted directed graph recursively """
    path = path + [start]
    length = length + steplength
    if start == end:
        return path, length
    if start > len(graph) - 1:
        return None
    shortest = None
    shortest_length = None

    # Iterate through all neighbours
    for i in range(0, len(graph[start])):

        if i not in path and graph[start][i] > 0:
            # Recursively find a new path from neighbour
            newpath, newlength = shortest_path_simple(graph, i, end, path,
                length, graph[start][i])
            if newpath:
                if not shortest_length or newlength < shortest_length:
                    shortest = newpath
                    shortest_length = newlength

    return shortest, shortest_length


def shortest_path_dijkstra(graph, start, end):
    """ Find the shortest path using Dijkstra's Algorithm """
    previous = [None] * len(graph)
    distance = [None] * len(graph)
    visited = [False] * len(graph)
    distance[start] = 0

    while True:
        # Find the unvisited node with the smallest distance
        current = get_smallest_entry(visited, distance)
        if current is None:
            # No path found
            return None, None
        if current is end:
            path = [current]
            while current is not start:
                # Reconstruct path
                path.append(previous[current])
                current = previous[current]
            return path[::-1], distance[end]

        for i in range(0, len(graph[current])):
            # Graph[current][i] contains the weight of the edge to i
            if graph[current][i] > 0 and not visited[i]:
                this_distance = distance[current] + graph[current][i]
                if distance[i] is None or this_distance < distance[i]:
                    distance[i] = this_distance
                    previous[i] = current
        visited[current] = True


def get_smallest_entry(visited, distance):
    """ Returns the position of the unvisited node with the smallest
    distance. Returns None if no options are left. """
    smallest = None
    smallest_entry = None

    for i in range(0, len(visited)):
        if not visited[i] and distance[i] is not None:
            if distance[i] < smallest or smallest is None:
                smallest_entry = i
                smallest = distance[i]

    return smallest_entry


if __name__ == '__main__':
    graph = create_random_graph(16)

    start = time.clock()
    path, length = shortest_path_simple(graph, 0, 4)
    end = (time.clock() - start)

    print "Recursive algorithm found path %s with length %d in %f seconds" % \
        (path, length, end)

    start = time.clock()
    path, length = shortest_path_dijkstra(graph, 0, 4)
    end = (time.clock() - start)

    print "Dijkstra's algorithm found path %s with length %d in %f seconds" % \
        (path, length, end)
