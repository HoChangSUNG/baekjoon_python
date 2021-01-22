from collections import deque
input_data = list(map(int, input().split()))
loc_per_time = [set() for _ in range(100001)]
def solution(s_loc,target_loc): # 숨바꼭질 -메모리 초과
    queue = deque()
    queue.append((s_loc,0))
    loc_per_time[0].add(s_loc)
    while queue:
        loc,time = queue.popleft()

        if 0<=loc-1 and loc-1 not in loc_per_time[time + 1]:
            loc_per_time[time + 1].add(loc-1)
            queue.append((loc-1,time+1))
        if loc + 1<=100000 and loc + 1 not in loc_per_time[time + 1]:
            loc_per_time[time + 1].add(loc + 1)
            queue.append((loc + 1, time + 1))
        if loc *2<=100000 and loc *2 not in loc_per_time[time + 1]:
            loc_per_time[time + 1].add(loc * 2)
            queue.append((loc * 2, time + 1))

        if target_loc in loc_per_time[time-1]:
            return time-1

print(solution(input_data[0],input_data[1]))