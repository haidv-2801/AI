from collections import defaultdict
import pretty_table_config as ptb

# Các tham số được sửa
FILE_IN = 'datain1.txt'
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
            a, b = [str(x) for x in line.split()]
            graph[a].append(b)
    for key in graph:
        graph[key] = sorted(graph[key])


def execute(st, ed):
    tb = ptb.get_table(['Phat trien TT', 'Trang thai ke', 'Danh sach L'])
    print("%s %40s" % ("\n", "Depth First Search"))
    print("Quan he:")
    stack = [st]
    visited = {}
    while stack:
        top = stack.pop()
        mid = ', '.join(str(x) for x in graph[top])

        if top == ed:
            tb.add_row([top, "TTKT - DUNG", ""])
            print(tb)
            print("Duong di:")
            res.append(st)
            print_path(st, ed)
            print('->'.join(res))
            return

        tb.add_row([str(top), mid, ' ,'.join(str(x) for x in (stack + graph[top]))[::-1]])
        for i in graph[top]:
            # if i not in visited:
            #     visited[i] = 1
                parent[i] = top
                stack.append(i)

    print('\nKhong tim thay!')


if __name__ == '__main__':
    make_graph(FILE_IN)
    execute(start, end)
