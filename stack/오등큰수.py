#  오등큰수, 계속 시간 초과 떠서 다른 사람 코드 참고
import sys
from collections import Counter

n = int(input())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
result = [-1 for _ in range(n)]
ngf = Counter(sequence)
for i in range(n):
    while stack and ngf[sequence[stack[-1]]] < ngf[sequence[i]]:
        result[stack[-1]] = sequence[i]
        stack.pop()
    stack.append(i)
for i in range(n):
    print(result[i], end=" ")



