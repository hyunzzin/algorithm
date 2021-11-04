'''
모든 토마토가 익어있으면 0 출력
모두 익지는 못하면 -1 출력 : 안익은 토마토가 있는 경우
익은 토마토 : 1
안익은 토마토 : 0
토마토가 없는 경우 : -1
1. 익은 토마토들을 전부 큐에 넣기
2. 하나씩 꺼내서 근처에 토마토가 있으면 큐에 넣어준다.
    -> 근처에 토마토가 없으면 넘어간다.
    -> 토마토가 익은 날짜는 현재 토마토의 숫자에 +1을 해서 넣는다.
3. 큐가 비면 출력한다.
'''
import sys
from collections import deque
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
que = deque()
M, N = map(int, sys.stdin.readline().split())
tom = []
# 익은 토마토 넣기
for _ in range(N):
    tom.append(list(map(int,sys.stdin.readline().split())))

def bfs():
    while que:
        cur = que.popleft()
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= N or x < 0 or y >= M or y < 0: continue                                                                                                                                                                 
            if tom[x][y] == 0:
                que.append((x,y))
                tom[x][y] = tom[cur[0]][cur[1]]+1

def check():
    ans = 0
    for i in range(N):
        for j in range(M):
            ans = max(ans, tom[i][j])
            if tom[i][j] == 0:
                return False
    return ans
            
for i in range(N):
        for j in range(M):
            if tom[i][j] == 1:
                que.append((i,j))
bfs()
ans = check()
if ans:
    print(ans-1)
else:
    print(-1)

