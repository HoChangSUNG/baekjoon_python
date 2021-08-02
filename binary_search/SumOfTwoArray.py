# 두 배열의 합 2143번
import sys

def binarySearch():
    cnt = 0
    arr1Index, arr2Index = 0, 0
    while arr1Index < len(arr1SumArr) and arr2Index < len(arr2SumArr):
        arrSum = arr1SumArr[arr1Index] + arr2SumArr[arr2Index]
        if arrSum == t:
            tempArr1Cnt,tempArr2Cnt = 1, 1
            arr1Index += 1
            arr2Index += 1
            while arr1Index < len(arr1SumArr) and arr1SumArr[arr1Index] == arr1SumArr[arr1Index-1] :
                arr1Index += 1
                tempArr1Cnt += 1
            while arr2Index < len(arr2SumArr) and  arr2SumArr[arr2Index] == arr2SumArr[arr2Index-1]:
                arr2Index += 1
                tempArr2Cnt += 1
            cnt += (tempArr1Cnt*tempArr2Cnt)
        elif arrSum > t:
            arr1Index += 1
        else:
            arr2Index += 1
    return cnt

t = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
arr1SumArr = list()
arr2SumArr = list()

for i in range(len(arr1)):
    arrSum = 0
    for j in range(i, len(arr1)):
        arrSum += arr1[j]
        arr1SumArr.append(arrSum)
arr1SumArr.sort(reverse=True)

for i in range(len(arr2)):
    arrSum = 0
    for j in range(i, len(arr2)):
        arrSum += arr2[j]
        arr2SumArr.append(arrSum)
arr2SumArr.sort()

print(binarySearch())