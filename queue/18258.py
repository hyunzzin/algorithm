# deque 모듈 없이 queue 구현
import sys
queue = []
n = int(sys.stdin.readline())
st = 0
bk = 0
for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'push':
        queue.append(cmd[1])
        bk+=1
    elif cmd[0] == 'pop':
        if st == bk:
            print(-1)
            continue
        print(queue[st])
        st+=1
    elif cmd[0] == 'size':
        print(bk-st)
    elif cmd[0] == 'empty':
        if st == bk:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if st == bk:
            print(-1)
        else:
            print(queue[st])
    elif cmd[0] == 'back':
        if st == bk:
            print(-1)
            continue
        else:
            print(queue[bk-1])
