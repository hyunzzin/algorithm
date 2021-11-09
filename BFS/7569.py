'''
토마토
저장될 때부터 모든 토마토가 익어있으면 0을 출력
토마토가 모두 익지 못하는 상황이면 -1 출력
'''
import sys
from collections import deque
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
M,N,H = map(int,sys.stdin.readline().split())
tom = []
'''
익은 토마토를 찾아서 que에 넣기
tom[h][c][r]
익은 토마토 : 1
안익은 토마토 : 0
토마토 없음 : -1
'''

for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int,sys.stdin.readline().split())))
    tom.append(temp)
que=deque()
for h in range(H):
    for c in range(N):
        for r in range(M):
            # 익은 토마토 que에 넣기
            if tom[h][c][r] == 1: 
                que.append((h,c,r))      
# 토마토 익히기
def tomato_bfs():
    while que:
        cur = que.popleft()
        for k in range(6):
            z = cur[0] + dz[k]
            x = cur[1] + dx[k]
            y = cur[2] + dy[k]
            if x<0 or x>=N or y<0 or y>=M or z<0 or z>=H: continue
            if tom[z][x][y] == 0: # 안익은 토마토가 있는 경우
                que.append((z,x,y))
                tom[z][x][y] = tom[cur[0]][cur[1]][cur[2]]+1

# 안익은 토마토가 있는지 검사하기
def check():
    ans = 0
    for h in range(H):
        for c in range(N):
            for r in range(M):
                ans = max(ans, tom[h][c][r])
                if tom[h][c][r] == 0:
                    return False
    return ans
tomato_bfs()
ans = check()
if ans:
    print(ans-1)
else:
    print(-1)
