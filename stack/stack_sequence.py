 #  스택 수열
import sys
n = int(input())
s = []
answer = []
count = 1
currect = True
for i in range(n):
    v = int(sys.stdin.readline())
    while v>=count:
        s.append(count)
        count+=1
        answer.append('+')
    if s[-1]==v:
        answer.append('-')
        s.pop()
    else:
        currect = False
        break
if currect:
    for i in range(len(answer)):
        print(answer[i])
else:
    print('NO')