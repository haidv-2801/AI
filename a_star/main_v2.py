from collections import defaultdict
from functools import reduce
import pretty_table_config as ptb

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
    return str(node[1]) + '_' + str(node[0])


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
        for i in graph:
            graph[i] = sorted(graph[i])


def execute(st, ed):
    tb = ptb.get_table(['TT', 'TTK', 'k(u,v)', 'h(v)', 'g(v)', 'f(v)', 'Danh sach L'])
    ct = 0
    cost = 0
    queue = [(f[st], st)]

    while queue:
        front = queue.pop(0)

        if front[1] == ed:
            cost = max(cost, f[front[1]])
            tb.add_row(
                ['---\n' + str(front[1]), *['---'] * 4,
                 f'---\nTTKT, tim duoc duong\n di tam thoi, do dai {f[front[1]]}',
                 '---'])
            ct += 1
            if ct == count:
                l = ', '.join([fm(x) for x in (queue)])
                tb.add_row([*['---'] * 6, l])
                print(tb)
                print("nếu dích có cost bằng nhau chỉ viết 1 lần")
                return
        else:
            tb.add_row(['---\n' + str(front[1]), *['---'] * 6])

        next_path = []
        for e in graph[front[1]]:
            g[e] = g[front[1]] + k[(front[1], e)]
            f[e] = g[e] + h[e]
            next_path.append((f[e], e))
            tb.add_row(['', e, k[front[1], e], h[e], g[e], f[e], ' '])

        if len(next_path) > 0:
            queue = sorted(next_path.copy() + queue)
        l = ', '.join([fm(x) for x in queue])
        tb.add_row([*[' '] * 6, l])
    print("Không đi được!")


if __name__ == '__main__':
    print("A Start")
    make_graph()
    execute(start, end)
