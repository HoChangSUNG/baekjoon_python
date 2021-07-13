# 용액, 2467번
import sys


def binary_search():
    for i in range(n - 1):
        startIndex = i + 1
        endIndex = len(liquid) - 1

        while startIndex <= endIndex:
            targetIndex = (startIndex + endIndex) // 2
            value = liquid[i] + liquid[targetIndex]

            if abs(sum(result)) > abs(liquid[i] + liquid[targetIndex]):
                result[0] = result[0] = liquid[i]
                result[1] = liquid[targetIndex]

            if value == 0:
                return
            elif value > 0:
                endIndex = targetIndex - 1
            else:
                startIndex = targetIndex + 1


n = int(sys.stdin.readline().rstrip())
liquid = list(map(int, sys.stdin.readline().rstrip().split()))
result = [1000000000, 1000000000]
binary_search()
print(*result)
