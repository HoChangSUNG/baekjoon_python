# 네트워크연결,1922번
import sys

def find_parent(n):
    parent_node=0
    if parent[n] == n:
        parent_node = n
    else:
        parent_node = find_parent(parent[n])
    return parent_node

def union_parent(n,m):
    parent[max(n,m)]=min(n,m)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
edge = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]
total_cost = 0
edge.sort(key=lambda x :x[2])

for node1,node2,cost in edge:
    p_node1 = find_parent(node1)
    p_node2 = find_parent(node2)
    if(p_node1!=p_node2):
        union_parent(p_node1,p_node2)
        # print(cost)
        total_cost+=cost


print(total_cost)