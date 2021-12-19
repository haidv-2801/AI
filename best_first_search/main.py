from queue import PriorityQueue
from collections import defaultdict
import pretty_table_config as ptb

# Các tham số được sửa
FILE_IN = 'datain.txt'
# Các tham số được sửa

source = None
target = None
graph = defaultdict(list)
v = 10000

def make_graph():
    global source, target, graph
    with open(FILE_IN) as f:
        source, target = [str(x) for x in next(f).split()]
        for line in f:
            a, b, cost = [str(x) for x in line.split()]
            graph[a].append((b, int(cost)))
            graph[b].append((a, int(cost)))

def best_first_search(source, target, n):
    visited = [0] * n
    visited = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))

if __name__ == '__main__':
    best_first_search(source, target, v)
