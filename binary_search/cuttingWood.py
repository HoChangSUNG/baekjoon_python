# 나무자르기,2805번
import sys

def binarySearch():
    getResultTree = sum(tree)
    maxHeight = 0
    startHeight = 0
    endHeigh = tree[0] - 1
    while startHeight <= endHeigh:
        getTree = 0
        midHeight = (startHeight + endHeigh) // 2
        for i in range(len(tree)):
            if midHeight >= tree[i]:
                break
            getTree += (tree[i] - midHeight)
        if getResultTree > getTree and getTree >= target:
            getResultTree = getTree
            maxHeight = midHeight

        if getTree == target:
            return maxHeight
        elif getTree > target:
            startHeight = midHeight + 1
        else:
            endHeigh = midHeight - 1

    return maxHeight

n, target = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
tree.sort(reverse=True)
print(binarySearch())