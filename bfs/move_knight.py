from collections import deque
dr = [1,1,-1,-1,2,2,-2,-2]
dc = [-2,2,2,-2,1,-1,1,-1]
def solution(chess_map,start_row,start_col,end_row,end_col): # 나이트의 이동
    chess_map[start_row][start_col]=1
    queue = deque()
    queue.append((start_row,start_col,0))
    while queue:
        row,col,cnt = queue.popleft()
        if row == end_row and col == end_col:
            return cnt
        for i in range(8):
            if -1< row+dr[i] <len(chess_map) and -1< col+dc[i] <len(chess_map):
                if chess_map[row+dr[i]][col+dc[i]] != 1:
                    chess_map[row+dr[i]][col+dc[i]] = 1
                    queue.append((row+dr[i],col+dc[i],cnt+1))

test_case = int(input())
for i in range(test_case):
    length = int(input())
    chess_map = [[0 for _ in range(length)]for _ in range(length)]

    s_r,s_c = map(int,input().split())
    e_r, e_c = map(int,input().split())
    print(solution(chess_map,s_r,s_c,e_r,e_c))