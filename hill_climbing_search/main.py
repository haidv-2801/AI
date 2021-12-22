from collections import defaultdict
from functools import reduce
import pretty_table_config as ptb

# Các tham số được sửa
FILE_IN = ptb.FILE_IN
BEGIN_COST = 30
# Các tham số được sửa

start = None
end = None
graph = defaultdict(list)
parent = {}
MAX_SIZE = int(1E6)
res = []


def f(node: tuple) -> str:  # (a,b) -> ba
    return str(str(node[1]) + '_' + str(node[0]))


def format_queue(queue):  # [[],[]] -> []
    if len(queue) > 0:
        return reduce(lambda a, b: a + b, queue)
    return []


def print_path(st, ed):
    if parent[ed] != st:
        print_path(st, parent[ed])
    res.append(ed)


def make_graph():
    global start, end, graph
    with open(FILE_IN) as f:
        start, end = [str(x) for x in next(f).split()]
        for line in f:
            a, w_a, b, cost, w_b  = [str(x) for x in line.split()]
            graph[a].append((int(cost), b))
        for key in graph:
            graph[key] = sorted(graph[key])


def execute(st, ed):
    tb = ptb.get_table(['Phat trien TT', 'Trang thai ke', 'Danh sach L1', 'Danh sach L'])

    print("\nHill Climbing Search:")
    path = [(BEGIN_COST, st)]
    queue = [path.copy()]
    while queue:  # queue: [[(cost),(to)], [(),()],]
        path = queue.pop(0)  # path: [(),()]
        path_front = path.pop(0)  # path_front: (cost, to)
        if len(path) > 0:  # not insert [] to queue
            queue.insert(0, path)

        sort = sorted(graph[path_front[1]])
        mid = 'TTKT Dung' if path_front[1] == ed else ', '.join(f(x) for x in graph[path_front[1]])
        L1 = '' if path_front[1] == ed else ', '.join(f(x) for x in sort)
        L = '' if path_front[1] == ed else ', '.join(f(x) for x in (sort + format_queue(queue)))
        tb.add_row([f(path_front), mid, L1, L])

        if path_front[1] == ed:
            print(tb)
            res.append(st)
            print_path(st, ed)
            print('->'.join(res))
            return
        next_path = []
        for next in graph[path_front[1]]:
            parent[next[1]] = path_front[1]
            next_path.append(next)
        if len(next_path) > 0:
            queue.insert(0, next_path)
    print("Khong di duoc")


if __name__ == '__main__':
    make_graph()
    execute(start, end)
