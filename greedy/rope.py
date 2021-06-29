# 로프, 2217번
import sys
n = int(sys.stdin.readline().rstrip())
weight=[]
result=[]
for _ in range(n):
    weight.append(int(sys.stdin.readline().rstrip()))
weight.sort(reverse=True)
for i in range(n):
    result.append(weight[i]*(i+1))

print(max(result))