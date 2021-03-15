 #  제로
import sys
k= int(input())
stack = []
for i in range(k):
    integer = int(sys.stdin.readline())
    if integer == 0:
        stack.pop()
    else:
        stack.append(integer)
print(sum(stack))