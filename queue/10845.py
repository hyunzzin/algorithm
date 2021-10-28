'''
큐 구현
명령의 수 N (1 <= N <= 10,000)
명령 정수
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
    만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다.
    만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다.
    만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

pop, append를 사용한 방법이 더 빠르고 메모리도 적게 든다.
'''
import sys
queue = [0 for _ in range(10000)]
n = int(sys.stdin.readline())
st = 0
bk = 0
for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'push':
        queue[bk] = cmd[1]
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
            continue
        print(queue[st])
    elif cmd[0] == 'back':
        if st == bk:
            print(-1)
            continue
        print(queue[bk-1])
