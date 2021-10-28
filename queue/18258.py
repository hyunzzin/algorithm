# deque 모듈 없이 queue 구현
from sys import stdin
queue = []
n = int(stdin.readline())
st = 0

for _ in range(n):
    cmd = list(map(str,stdin.readline().split()))
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if st == len(queue):
            print(-1)
            continue
        print(queue[st])
        st+=1
    elif cmd[0] == 'size':
        print(len(queue)-st)
    elif cmd[0] == 'empty':
        if st == len(queue):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if st == len(queue):
            print(-1)
        else:
            print(queue[st])
    elif cmd[0] == 'back':
        if st == len(queue):
            print(-1)
            continue
        else:
            print(queue[-1])
