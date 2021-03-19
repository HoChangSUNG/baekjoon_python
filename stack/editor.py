 #  에디터,1406번
import sys
def editor(string,op):
    stack = []
    for i in range(len(op)):
        if op[i][0]=='L':
            if string:
                stack.append(string.pop())
        elif op[i][0]=='D':
            if stack:
                string.append(stack.pop())
        elif op[i][0]=='B':
            if string:
                string.pop()
        elif op[i][0]=='P':
            string.append(op[i][1])
    while stack:
        string.append(stack.pop())
    print("".join(string))
string = list(input())
n = int(input())
op = []
for i in range(n):
    op.append(sys.stdin.readline().rstrip().split())
editor(string,op)