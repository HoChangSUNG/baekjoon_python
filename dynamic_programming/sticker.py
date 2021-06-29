 #  스티커, 9465번
import sys
def max_num_of_sticker(sticker):
    dp=[[],[]]
    dp[0].append(sticker[0][0])
    dp[1].append(sticker[1][0])

    for j in range(1,len(sticker[0])):
            dp[0].append(max(dp[0][j-1],dp[1][j-1]+sticker[0][j]))
            dp[1].append(max(dp[1][j-1],dp[0][j-1]+sticker[1][j]))

    return max(dp[0][-1],dp[1][-1])
loop = int(input())
for _ in range(loop):
    col = int(input())
    sticker = []
    sticker.append(list(map(int,sys.stdin.readline().rstrip().split())))
    sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(max_num_of_sticker(sticker))