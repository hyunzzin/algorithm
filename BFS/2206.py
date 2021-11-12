'''
0 : 이동 가능
1 : 벽
'''
import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M = map(int, sys.stdin.readline().split())

mapp = []
for _ in range(N):
    mapp.append(list(map(int, sys.stdin.readline().strip('\n'))))
que = deque([(0,0,False)])
mapp[0][0] = 2

ans = 0

while que:
    ans +=1
    for i in range(len(que)):
        x,y,wall = que.popleft()

        if x == N-1 and y == M-1:
            print(ans)
            sys.exit()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx<0 or nx>=N or ny<0 or ny>=M: continue
            if wall: # 벽이 존재하면서
                if not mapp[nx][ny]: # 이동가능하면
                    mapp[nx][ny] = 3
                    que.append((nx,ny,wall))
            else:
                if not mapp[nx][ny]: # 벽이 존재하지 않으면
                    mapp[nx][ny] = 2
                    que.append((nx,ny,wall))
                    
                elif mapp[nx][ny] == 1: # 이동한 좌표에 벽이 있으면 
                    que.append((nx,ny,True))
                    
                elif mapp[nx][ny] == 3: # 
                    mapp[nx][ny] = 2
                    que.append((nx,ny,wall))

print(-1)

