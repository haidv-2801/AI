from collections import defaultdict
from functools import reduce
from AI.pretty_table_config import get_table

#Các tham số được sửa
FILE_IN = 'datain.txt'
#Các tham số được sửa

start = None
end = None
graph = defaultdict(list)
count = 0
k = {}
h = {}
g = {}
f = {}
parent = {}


def fm(node: tuple) -> str:  # (a,b) -> ba
    return str(str(node[1]) + '_' + str(node[0]))


def format_queue(queue):  # [[],[]] -> []
    if len(queue) > 0:
        return reduce(lambda a, b: a + b, queue)
    return []


def make_graph():
    global start, end, graph, k, h, g, f, count
    with open(FILE_IN) as fi:
        start, end = [str(x) for x in next(fi).split()]
        f[start] = 0
        f[end] = 0
        g[start] = 0
        g[end] = 0
        for line in fi:
            a, b, c, d, e = [str(x) for x in line.split()]
            h[a] = int(b)
            h[c] = int(d)
            f[a] = 0
            f[c] = 0
            g[a] = 0
            g[c] = 0
            k[(a, c)] = int(e)
            graph[a].append(c)
            if c == end:
                count += 1
        # sort cạnh kề
        # for i in graph:
        #     graph[i] = sorted(graph[i])


def bfs(st, ed):
    tb = get_table(['TT', 'TTK', 'k(u,v)', 'h(v)', 'g(v)', 'f(v)', 'DS L1', 'Danh sach L'])
    ct = 0
    cost = 0
    path = [(f[st], st)]
    queue = [path.copy()]

    while queue:
        path = queue.pop(0)
        front = path.pop(0)

        if len(path) > 0:  # not insert [] to queue
            queue.insert(0, path)

        if front[1] == ed:
            tb.add_row(
                ['---\n' + str(front[1]), *['---'] * 5,
                 f'---\nTTKT, tim duoc duong di tam thoi, do dai {f[front[1]]}',
                 '---'])
            cost = max(cost, f[front[1]])
            ct += 1
            if ct == count:
                l = ', '.join([fm(x) for x in format_queue(queue)])
                tb.add_row([*['---'] * 7, l])
                print(tb)
                return
        else:
            tb.add_row(['---\n' + str(front[1]), *['---'] * 7])

        next_path = []
        for e in graph[front[1]]:
            g[e] = g[front[1]] + k[(front[1], e)]
            f[e] = g[e] + h[e]
            next_path.append((f[e], e))
            tb.add_row(['', e, k[front[1], e], h[e], g[e], f[e], ' ', ' '])

        if len(next_path) > 0:
            queue.insert(0, sorted(next_path.copy()))

        l1 = ', '.join([fm((f[x], x)) for x in sorted(graph[front[1]])])
        l = ', '.join([fm(x) for x in format_queue(queue)])
        tb.add_row([*[' '] * 6, l1, l])
    print("Không đi được!")


if __name__ == '__main__':
    print("Branch and bound")
    make_graph()
    bfs(start, end)
