# 쇠막대기,10799번
import sys

parentheses = sys.stdin.readline().rstrip()
stack=[]
cnt = 0
for i in range(len(parentheses)):
    if parentheses[i]=='(':
        stack.append(i)
    else:
        if stack[-1]+1 == i:
            stack.pop()
            cnt+=len(stack)
        else:
            cnt +=1
            stack.pop()
print(cnt)