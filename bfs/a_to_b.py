from collections import deque
def bfs(start,end):  # A -> B
    queue = deque()
    queue.append((start,0))

    while queue:
        num , cnt = queue.popleft()
        if num == end:
            return cnt+1
        if 2*num<=end and 2*num<=end : # 2를 곱한다
            queue.append((2*num,cnt+1))

        if num*10+1<=end and num*10+1 :  # 1을 수의 가장 오른쪽에 추가한다.
            queue.append((num*10+1,cnt+1))

    return -1

start, end = map(int,input().split())
print(bfs(start,end))