from collections import deque
input_data = list(map(int, input().split()))

def solution(start,end):# 숨바꼭질 2
    queue = deque()
    queue.append((0,start)) # time,start
    visited = [-1 for _ in range(100001)]
    cnt = 0
    max_time = float('INF')
    while queue:
        time, loc = queue.popleft()
        visited[loc] = time
        if time > max_time:
            break
        if loc == end :
            cnt += 1
            if cnt == 1:
                max_time = time
        if loc-1 >= 0 and visited[loc-1] == -1:
            queue.append((time+1, loc-1))
        if loc+1 <= 100000 and visited[loc+1] == -1:
            queue.append((time + 1, loc + 1))
        if loc*2 <= 100000 and visited[loc*2] == -1:
            queue.append((time + 1, loc * 2))
    print(max_time,cnt)
solution(input_data[0], input_data[1])
