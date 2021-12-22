from collections import defaultdict
from functools import reduce
import pretty_table_config as ptb

# Các tham số được sửa
FILE_IN = ptb.FILE_IN
# Các tham số được sửa

start = None
end = None
graph = defaultdict(list)
k = {}
h = {}
g = {}
f = {}
parent = []


def fm(node: tuple) -> str:  # (a,b) -> ba
    return str(node[1]) + '_' + str(node[0])

def make_graph():
    global start, end, graph, k, h, g, f
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
        # sort cạnh kề
        # for i in graph:
        #     graph[i] = sorted(graph[i])
        # print(graph)


def execute(st, ed):
    tb = ptb.get_table(['TT', 'TTK', 'k(u,v)', 'h(v)', 'g(v)', 'f(v)', 'Danh sach L'])
    ct = 0
    queue = [(f[st], st)]

    while queue:
        front = queue.pop(0)
        parent.append(front[1])
        if front[1] == ed:
            tb.add_row(
                ['---\n' + str(front[1]), *['---'] * 4,
                 f'---\nTTKT, tim duoc duong\n di tam thoi, do dai {f[front[1]]}',
                 '---'])

            l = ', '.join([fm(x) for x in (queue)])
            print(tb)
            print('->'.join(parent))
            return

        else:
            tb.add_row(['---\n' + str(front[1]), *['---'] * 6])

        for e in graph[front[1]]:
            g[e] = g[front[1]] + k[(front[1], e)]
            f[e] = g[e] + h[e]
            queue.append((f[e], e))
            tb.add_row(['', e, k[front[1], e], h[e], g[e], f[e], ' '])

        queue = sorted(queue)
        l = ', '.join([fm(x) for x in queue])
        tb.add_row([*[' '] * 6, l])
    print("Không đi được!")


if __name__ == '__main__':
    print("A Start")
    make_graph()
    execute(start, end)
