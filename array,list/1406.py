'''
import sys
word = list(input())
m = int(input())
cur = len(word)
for _ in range(m):
    com = list(map(str, sys.stdin.readline().split()))
    if com[0] == 'P':
        word.insert(cur,com[1])
        cur += 1
    elif cur != 0 and com[0] == 'L':
        cur -= 1
    elif cur != len(word) and com[0] == 'D':
        cur += 1
    elif cur != 0 and com[0] == 'B':
        del word[cur-1]
        cur -= 1
print(''.join(word))

import time
import sys
st1 = list(input())
st2 = []
m = int(input())
start_time = time.time()
for _ in range(m):
    com = sys.stdin.readline()
    if com[0] == 'P':
        st1.append(com[2])
    elif st1 and com[0] == 'L':
        st2.append(st1.pop())
    elif st2 and com[0] == 'D':
        st1.append(st2.pop())
    elif st1 and com[0] == 'B':
        st1.pop()

word = ''.join(st1)
for i in range(len(st2)-1,-1,-1):
    word += st2[i]
print(word)
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

# if -> elif로 바꾸면 100ms 줄음
# len을 안쓰면 60ms 줄음
# map을 안쓰면 또 줄어버린다.
'''
import time
import sys
st1 = list(input())
st2 = []
m = int(input())
start_time = time.time()
for _ in range(m):
    com = sys.stdin.readline()
    if com[0] == 'P':
        st1.append(com[2])
    elif st1 and com[0] == 'L':
        st2.append(st1.pop())
    elif st2 and com[0] == 'D':
        st1.append(st2.pop())
    elif st1 and com[0] == 'B':
        st1.pop()
print(''.join(st1) + ''.join(reversed(st2)))
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

