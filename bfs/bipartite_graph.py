from collections import deque
def solution(graph):  # 이분 그래프
    bipartite = [-1 for _ in range(len(graph)+1)]  #방문x -> -1 , 방문 o -> 0 or 1(색깔)
    queue= deque()
    queue.append(1) # 1번 노드부터 탐색 시작
    bipartite[1]+=1 # 1번 노드의 색깔을 0으로
    while queue:
        node = queue.popleft()
        for adjacent_node in graph[node]:
            if bipartite[adjacent_node]==-1: # bipartite[node] = 1 -> bipartite[adjacent_node] = 0, bipartite[node] = 0 -> bipartite[adjacent_node] = 1
                bipartite[adjacent_node] = (bipartite[node]+1)%2
                queue.append(adjacent_node)
            elif bipartite[adjacent_node] == bipartite[node]: # 이분 그래프가 아니라면

                return 'NO'
        if len(queue)==0:
            for node in range(1,len(graph)+1):
                if bipartite[node]== -1: # 아직 탐색하지 않은 노드가 있다면
                    bipartite[node]+=1
                    queue.append(node)
                    break
    return 'YES'
loop = int(input())
for i in range(loop):
    v,e = map(int,input().split())
    graph = {i:[] for i in range(1,v+1)}
    for i in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(solution(graph))

