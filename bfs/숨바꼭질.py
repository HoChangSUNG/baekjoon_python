from collections import deque
input_data = list(map(int, input().split()))

def solution(s_loc,b_loc): # 숨바꼭질 -성공
    visited = {s_loc}
    queue = deque()
    queue.append((s_loc,0)) # 수빈이 위치, 초
    while queue:
        s_loc,time = queue.popleft()
        # print(s_loc,time)
        if s_loc == b_loc:
            return time
        if 0<=s_loc - 1<=100000 and s_loc-1 not in visited:
            queue.append((s_loc-1,time+1))
            visited.add(s_loc-1)
        if 0<=s_loc + 1<=100000 and s_loc+1 not in visited:
            queue.append((s_loc +1 , time + 1))
            visited.add(s_loc + 1)
        if 0<=s_loc*2<=100000 and s_loc*2 not in visited:
            queue.append((s_loc *2, time + 1))
            visited.add(s_loc * 2)




print(solution(input_data[0],input_data[1]))