# 다이어트, 19942번
import sys

cost = float('inf')
result = []
n = int(sys.stdin.readline())
leastNutrition = list(map(int,sys.stdin.readline().rstrip().split()))
nutritions = []
for _ in range(n):
    nutritions.append(list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(1,1<<n):
    curNutrition = [0 for _ in range(5)]
    curResult = []
    for j in range(n):
        if i&(1<<j)>0:
            curResult.append(j+1)

            curNutrition[0] += nutritions[j][0]
            curNutrition[1] += nutritions[j][1]
            curNutrition[2] += nutritions[j][2]
            curNutrition[3] += nutritions[j][3]
            curNutrition[4] += nutritions[j][4]
    for j in range(4):
        if curNutrition[j]<leastNutrition[j]:
            break
    else:
        if cost>curNutrition[4]:
            result = [curResult]
            cost = curNutrition[4]
        elif cost == curNutrition[4]:
            result.append(curResult)
if cost==float('inf'):
    print(-1)
else:
    print(cost)
    result.sort()
    print(*result[0])