 #  가장 큰 정사각형
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,list(input()))))
answer = []

for i in range(1,n):
    for j in range(1,m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1]) + 1

for i in range(n):
    answer.append(max(arr[i]))
print(max(answer)**2)