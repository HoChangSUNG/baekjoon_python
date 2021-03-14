 #  키로거, 5397번
import sys
def get_password(key_logger):
    left = []
    right = []
    for key in key_logger:
        if key=='<':
            if left:
                right.append(left.pop())
        elif key=='>':
            if right:
                left.append(right.pop())
        elif key=='-':
            if left:
                left.pop()
        else:
            left.append(key)
    return "".join(left)+"".join(right[::-1])


n= int(input())
for _ in range(n):
    key_logger = sys.stdin.readline().rstrip()
    print(get_password(key_logger))
