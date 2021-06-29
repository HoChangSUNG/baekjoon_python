 #  오큰수, 오등큰수 문제와 같은 유형
import sys
n = int(input())
s= list(map(int,sys.stdin.readline().split()))
stack = []
answer = [-1 for _ in range(n)]
for i in range(n):
    while stack and s[stack[-1]]<s[i]:
        answer[stack[-1]] = s[i]
        stack.pop()
    stack.append(i)
for i in range(n):
    print(answer[i],end=" ")