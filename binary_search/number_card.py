# 숫자카드 10815번
import sys
def binarySearch(target):
    startIndex = 0
    endIndex = n-1
    while startIndex <= endIndex:
        targetIndex = (startIndex+endIndex)//2
        if target == cards[targetIndex]:
            return 1
        elif target>cards[targetIndex]:
            startIndex = targetIndex+1
        else :
            endIndex = targetIndex-1
    return 0

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
targetCards = list(map(int, sys.stdin.readline().rstrip().split()))
cards.sort()
for i in range(m):
    print(binarySearch(targetCards[i]),end = " ")
