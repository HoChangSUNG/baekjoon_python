# 단어 나누기, 1251번
import sys

word = sys.stdin.readline().rstrip()
words = []

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        words.append(word[:i][::-1]+word[i:j][::-1]+word[j:][::-1])
words.sort()
print(words[0])