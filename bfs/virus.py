from collections import deque
number = int(input())
edge_num = int(input())
adjacent_graph = {}
for i in range(1,number+1):
    adjacent_graph[i] = []
for i in range(edge_num):
    a, b = list(map(int,input().split()))
    adjacent_graph[a].append(b)
    adjacent_graph[b].append(a)

# print(adjacent_graph)
def solution(adjacent_graph): # 바이러스
    queue = deque()
    queue.append(1) # 1번 노드부터 시작
    visited = set()
    visited.add(1)
    while queue: # 인접한 노드 방문
        cur_node = queue.popleft()
        for adjacent_node in adjacent_graph[cur_node]:
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                queue.append(adjacent_node)
    # print("방문한노드",visited)  #방문한 노드
    print(len(visited)-1) # 방문한 노드 -1 (1번 노드를 제외하기 위함.)

solution(adjacent_graph)