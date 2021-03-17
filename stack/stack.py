 #  스택, 10828번
import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.empty()==1:
            return -1
        pop_value = self.head.data
        self.head = self.head.next
        return pop_value
    def size(self):
        if self.empty()==1:
            return 0
        cur_node = self.head
        cnt=1
        while cur_node.next is not None:
            cur_node = cur_node.next
            cnt+=1
        return cnt
    def empty(self):
        if self.head is None:
            return 1
        else:
            return 0
    def top(self):
        if self.head is None:
            return -1
        return self.head.data
    def print_all(self):
        if self.empty()==1:
            return
        else:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.data)
                cur_node = cur_node.next
stack = Stack()
n = int(input())
for _ in range(n):
    com = sys.stdin.readline().rstrip().split()
    if com[0]=='push':
        stack.push(int(com[1]))
    elif com[0]=='pop':
        print(stack.pop())
    elif com[0]=='size':
        print(stack.size())
    elif com[0]=='empty':
        print(stack.empty())
    elif com[0] == 'top':
        print(stack.top())

