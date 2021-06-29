import sys
m = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(m)]
number=9
words_sum=0
alphabet_num = [-1]*26
words.sort(key=lambda word : len(word),reverse=True)

for i in range(len(words[0])):
    for j in range(len(words)):
        if len(words[0]) - len(words[j])>i:
            break
        word_index=i-len(words[j])
        alphabet = words[j][word_index]
        alphabet_num_index = ord(alphabet)-ord('A')
        if alphabet_num[alphabet_num_index]==-1:
            alphabet_num[alphabet_num_index]=number
            number=number-1

for i in range(len(words)):
    convert = 0
    for j in range(0,len(words[i])):
        convert*=10
        alphabet = words[i][j]
        alphabet_num_index = ord(alphabet)-ord('A')
        convert+= alphabet_num[alphabet_num_index]
    print(convert)
    words_sum+=convert
print(words_sum)

print(alphabet_num)