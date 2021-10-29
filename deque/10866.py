'''
deque 구현하기

deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
deque.remove(item): item을 데크에서 찾아 삭제한다.
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
'''
from collections import deque
import sys
deq = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        deq.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
        
