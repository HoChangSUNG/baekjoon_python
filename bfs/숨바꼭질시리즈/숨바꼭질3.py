from collections import deque
input_data = list(map(int, input().split()))

def solution(start_loc,target_loc):#숨바꼭질3
    queue = deque()
    queue.append((0,start_loc))  # 시간 현재 위치
    visited = [-1 for _ in range(100001)]  # 해당 위치에 도달하는데 걸리는 시간
    visited[start_loc] = 0  # 시작 위치는 0초후 도달 가능
    min = float('INF')
    while queue:
        time,cur_loc = queue.popleft()
        # print(time,cur_loc)
        if cur_loc *2 <= 100000 and visited[cur_loc * 2] == -1 :
            visited[cur_loc * 2] = time
            queue.appendleft((time, cur_loc*2))

        if cur_loc == target_loc:

            if min>time:
                min=time

        if cur_loc -1 >= 0 and visited[cur_loc -1] == -1:
            visited[cur_loc - 1] = time + 1
            queue.append((time+1, cur_loc-1))
        if cur_loc+1 <= 100000 and visited[cur_loc +1] == -1:
            visited[cur_loc + 1] = time + 1
            queue.append((time + 1, cur_loc + 1))

    print(min)
solution(input_data[0],input_data[1])