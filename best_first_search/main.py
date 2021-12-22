from queue import PriorityQueue
from collections import defaultdict
import pretty_table_config as ptb

# Các tham số được sửa
FILE_IN = ptb.FILE_IN
BEGIN_COST = 30
# Các tham số được sửa

source = None
target = None
graph = defaultdict(list)
visited = {}


def make_graph():
    global source, target, graph
    with open(FILE_IN) as f:
        source, target = [str(x) for x in next(f).split()]
        for line in f:
            a, w_a, b, cost, w_b  = [str(x) for x in line.split()]
            graph[a].append((int(cost), b))
        # for i in graph:
        #     i = sorted(i)


def f(node: tuple) -> str:  # (a,b) -> ba
    return str(str(node[1]) + '_' + str(node[0]))


def best_first_search(source, target):
    tb = ptb.get_table(["Phat trien TT", "Trang thai ke", "Danh sach L"])
    pq = [(BEGIN_COST, source)]
    while pq:
        u = pq[0]
        pq = pq[1:]
        if u[1] == target:
            tb.add_row([f(u), "TTKT - Dung", ''])
            print(tb)
            return
        l = sorted(pq + graph[u[1]])
        l = ', '.join([f(x) for x in l])
        l1 = ', '.join([f(x) for x in graph[u[1]]])
        tb.add_row([f(u), l1, l])
        pq = sorted(pq + graph[u[1]])
    print("\nKhong di duoc")


if __name__ == '__main__':
    print("Best First Search")
    make_graph()
    best_first_search(source, target)
