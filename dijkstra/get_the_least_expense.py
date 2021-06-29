# 최소비용 구하기, 1916번

import sys
from queue import PriorityQueue
def dijkstra(start):
    pq = PriorityQueue()
    cost = [float('INF') for i in range(n+1)]
    pq.put([0,start])
    while not pq.empty():
        cur_cost,cur_node = pq.get()
        if cur_cost>cost[cur_node]:
            continue
        for next_cost,next_node in graph[cur_node]:
            if cost[next_node]>next_cost+cur_cost:
                pq.put([next_cost+cur_cost,next_node])
                cost[next_node] = next_cost + cur_cost
    return cost
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = {i:[]for i in range(1,n+1)}

for i in range(m):
    from_node,to_node,cost = map(int, sys.stdin.readline().rstrip().split())
    graph[from_node].append([cost,to_node])
start_node, target_node = map(int,sys.stdin.readline().rstrip().split())
cost = dijkstra(start_node)
print(cost[target_node])