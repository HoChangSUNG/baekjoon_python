# 좋은 단어, 3986번

import sys
def isGoodWord(word):
    stack = []
    for char in word:
        if not stack or stack[-1]!=char:
            stack.append(char)
        else:
            stack.pop()
    return len(stack)==0

n = int(sys.stdin.readline().rstrip())
cnt=0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if isGoodWord(word) :
        cnt+=1
print(cnt)
