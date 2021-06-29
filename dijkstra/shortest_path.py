# 최단 경로, 1753번
import sys
from queue import PriorityQueue

def dik(graph,k,n):
    dist = [float('inf') for _ in range(n+1)]
    pq = PriorityQueue()
    pq.put((0,k)) #걸린시간,노드
    dist[k]=0
    while not pq.empty():
        cur_distance,cur_node = pq.get()
        if dist[cur_node]<cur_distance:
            continue
        for next_node,weight in graph[cur_node]:
            next_distance = cur_distance+weight
            if dist[next_node]>next_distance:
                dist[next_node] = next_distance
                pq.put((next_distance,next_node))
    return dist

V,E = map(int,sys.stdin.readline().rstrip().split())
k =  int(sys.stdin.readline().rstrip())
graph = [[]for _ in range(V+1)]
for _ in range(E):
    v,e,w = map(int,sys.stdin.readline().rstrip().split())
    graph[v].append([e,w])

diskr = dik(graph,k,V)
for d in diskr[1:]:
    if d == float('inf'):
        print('INF',end=' ')
    else:
        print(d,end=' ')