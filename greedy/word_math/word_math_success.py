# 단어 수학, 1339
import sys
m = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(m)]
words_frequency = {}
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] not in words_frequency :
            words_frequency[words[i][j]] = 0
        words_frequency[words[i][j]] += 10 ** (len(words[i]) - 1 - j)

sorted_list = sorted(words_frequency.items(),key=lambda x:x[1],reverse=True)
result,num = 0,9
for alphabet,frequency in sorted_list:
    result+=frequency*num
    num-=1
print(result)