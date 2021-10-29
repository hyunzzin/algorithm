from collections import deque
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    t = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip('[]\n').split(',')
    x = deque(arr)
    flag = 1
    dirc= False
    
    if n == 0: # 예외처리
        x = []
    
    for i in t:
        if i == 'R': # 뒤집기
            dirc = not(dirc)
        elif i == 'D': # 버리기
            if len(x) < 1:
                print('error')
                flag = 0
                break
            else:
                if dirc:
                    x.pop()
                else:
                    x.popleft()
    if dirc:
        x.reverse()
    if flag:
        print('[',end='')
        print(','.join(x),end='')
        print(']')
