#최소 스패닝 트리, 1197번
import sys
sys.setrecursionlimit(2000)

v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(0, v + 1)]
edge = []
for i in range(e):
    edge.append(list(map(int, sys.stdin.readline().rstrip().split())))


def find_parent(i):
    if parent[i] == i:
        return i
    return find_parent(parent[i])

def union(i, j):
    i_parent = find_parent(i)
    j_parent = find_parent(j)
    if j_parent < i_parent:
        parent[i_parent] = j_parent
    else:
        parent[j_parent] = i_parent


edge.sort(key=lambda x: x[2])
cnt, weight = 0, 0
for v1, v2, w in edge:
    if find_parent(v1) != find_parent(v2):
        union(v1, v2)
        weight = weight + w
print(weight)
