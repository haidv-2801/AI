from collections import defaultdict
import pretty_table_config as ptb

# Các tham số được sửa
FILE_IN = ptb.FILE_IN
# Các tham số được sửa

start, end = None, None
parent = {}
graph = defaultdict(list)
res = []


def print_path(st, ed):
    if parent[ed] != st:
        print_path(st, parent[ed])
    res.append(ed)


def make_graph(path):
    global start, end, graph
    with open(path) as f:
        start, end = [str(x) for x in next(f).split()]
        for line in f:
            a, w_a, b, w_b, cost = [str(x) for x in line.split()]
            graph[a].append(b)
    for key in graph:
        graph[key] = sorted(graph[key])


def execute(st, ed):
    tb = ptb.get_table(['Phat trien TT', 'Trang thai ke', 'Danh sach L'])
    print("%s %45s" % ("\n", "Breadth First Search"))
    print("Quan he:")

    queue = [st]
    visited = {}
    while queue:
        front = queue.pop(0)
        mid = ', '.join(str(x) for x in graph[front])

        if front == ed:
            tb.add_row([front, "TTKT - DUNG", ""])
            print(tb)
            print("Duong di:")
            res.append(st)
            print_path(st, ed)
            print('->'.join(res))
            return

        tb.add_row([str(front), mid, ', '.join(str(x) for x in (queue + graph[front]))])

        for i in graph[front]:
            # if i not in visited:
            #     visited[i] = 1
                if i not in parent:
                    parent[i] = front
                queue.append(i)

    print('\nKhong tim thay!')


if __name__ == '__main__':
    make_graph(FILE_IN)
    execute(start, end)
