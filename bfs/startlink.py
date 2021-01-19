from collections import deque
input_data = list(map(int,input().split()))
def solution(max_floor,cur_floor,target_floor,up,down): # 스타트링크
    queue = deque()
    queue.append((cur_floor,0))
    visited = {cur_floor}
    while queue:
        cur_floor, cnt = queue.popleft()
        if cur_floor == target_floor:
            return cnt
        temp_up_floor = cur_floor + up
        temp_down_floor = cur_floor - down
        if temp_up_floor<=max_floor and temp_up_floor not in visited:
            queue.append((temp_up_floor,cnt+1))
            visited.add(temp_up_floor)
        if 1<=temp_down_floor and temp_down_floor not in visited:
            queue.append((temp_down_floor,cnt+1))
            visited.add(temp_down_floor)
    return "use the stairs"

answer = solution(input_data[0],input_data[1],input_data[2],input_data[3],input_data[4])
print(answer)