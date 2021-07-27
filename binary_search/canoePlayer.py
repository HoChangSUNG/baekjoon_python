# 카누 선수, 9007번
import sys
def binarySearch():
    result = 999999999
    descIndex,ascIndex = 0,0
    while descIndex<len(descList) and ascIndex<len(ascList):
        weight = descList[descIndex]+ascList[ascIndex]
        if abs(k - result) > abs(k - weight):
            result = weight
        elif abs(k - result) == abs(k - weight):
            result = min(result,weight)

        if k==weight:
            return weight
        elif k>weight:
            ascIndex+=1
        else:
            descIndex+=1
    return result
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k, n = map(int,sys.stdin.readline().rstrip().split())
    class1 = list(map(int,sys.stdin.readline().rstrip().split()))
    class2 = list(map(int,sys.stdin.readline().rstrip().split()))
    class3 = list(map(int,sys.stdin.readline().rstrip().split()))
    class4 = list(map(int,sys.stdin.readline().rstrip().split()))
    descList,ascList = [],[]
    for i in range(len(class1)):
        for j in range(len(class2)):
            descList.append(class1[i]+class2[j])
    for i in range(len(class3)):
        for j in range(len(class4)):
            ascList.append(class3[i]+class4[j])

    descList.sort(reverse=True)
    ascList.sort()
    print(binarySearch())
