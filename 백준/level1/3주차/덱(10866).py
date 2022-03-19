import sys
from collections import deque

n=int(input())

stack=[]
queue=deque(stack)
for i in range(n):
    cmd=sys.stdin.readline().split()

    if cmd[0]=="push_front":
        queue.appendleft(cmd[1])  # queue.insert(0,cmd[1])
        
    elif cmd[0]=="push_back":
        queue.append(cmd[1])
        
    elif cmd[0]=="pop_front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
            
    elif cmd[0]=="pop_back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop())
            
    elif cmd[0]=="size":
        print(len(queue))

    elif cmd[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
            
    elif cmd[0]=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0]=="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
