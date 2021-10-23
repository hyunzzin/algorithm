'''
스택 구현하기
명령
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
    만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다.
    만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

명령의 수 N(1<=N<=10,000)
정수 k (1<=k<=100,000)
'''
import sys
n = int(sys.stdin.readline())
idx = 0
result = [0 for _ in range(10000)]
for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    # push
    if cmd[0] == 'push':
        result[idx]= int(cmd[1])
        idx+=1
    # pop
    elif cmd[0] == 'pop':
        if bool(idx):
            print(result[idx-1])
            idx-=1
        else:
            print(-1)
    # size
    elif cmd[0] == 'size':
        print(idx)
    # empty
    elif cmd[0] == 'empty':
        if bool(idx):
            print(0)
        else:
            print(1)
    # top
    elif cmd[0] == 'top':
        if bool(idx):
            print(result[idx-1])
        else:
            print(-1)
