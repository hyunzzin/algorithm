# deque 모듈 없이 queue 구현
"""
파이썬 3.5에서 32비트 정수는 28바이트를 소비한다.
그에 비해 문자열은 50바이트를 소비한다.
따라서 push를 할 때 문자형태의 숫자라면 정수형으로 변환함으로써 메모리를 적게 사용할 수 있다.
"""
from sys import stdin

queue = []
n = int(stdin.readline())
st = 0
for _ in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))  # 메모리 120208kb -> 91056kb 절감
    elif cmd[0] == "pop":
        if st == len(queue):
            print(-1)
            continue
        print(queue[st])
        st += 1
    elif cmd[0] == "size":
        print(len(queue) - st)
    elif cmd[0] == "empty":
        if st == len(queue):
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if st == len(queue):
            print(-1)
        else:
            print(queue[st])
    elif cmd[0] == "back":
        if st == len(queue):
            print(-1)
            continue
        else:
            print(queue[-1])
