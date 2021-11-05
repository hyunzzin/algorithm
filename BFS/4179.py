'''
불
지훈, 불 - 한칸씩 이동
지훈이는 맨끝에서 탈출할 수 있다
# : 벽
. : 지나갈 수 있는 공간
J : 지훈이의 초기위치
F : 불이 난 공간

미로를 탈출하지 못하는 경우 IMPOSSIBLE 출력
미로를 탈출할 수 있는 경우에는 가장 빠른 시간 출력

불을 먼저 bfs하고 불이 번진 시간을 기록한다.

'''
# 시간초과
# 숫자가 아닌 str이 있는 BFS라면 방문 배열을 따로 생성
import sys
from collections import deque
miro = []
que=deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
jh = 0 # 지훈이 위치
fire = [[False for _ in range(5)] for _ in range(5)]
R, C = map(int, sys.stdin.readline().split())
for i in range(R):
    miro.append(list(sys.stdin.readline().strip('\n')))
def bfs():
    while que:
        cur = que.popleft()
        for i in range(4):
            x = cur[0]+dx[i]
            y = cur[1]+dy[i]
            if x >= R or x < 0 or y >= C or y < 0: continue
            if miro[x][y] == '#' or (fire[x][y] >= 0 and type(fire[x][y])==int): continue # 이미 불이 있거나 벽, 지훈, 불 처음인 경우
            fire[x][y] = fire[cur[0]][cur[1]]+1
            que.append((x,y))

def esc():
    que.append(jh)
    cur = 0
    while que:
        cur = que.popleft()
        if cur[0] == R-1 or cur[1] == C-1 or cur[0] == 0 or cur[1] == 0:
            return cur
        for i in range(4):
            x = cur[0]+dx[i]
            y = cur[1]+dy[i]
            if x >= R or x < 0 or y >= C or y < 0 : continue
            if miro[x][y] == '#' or(fire[x][y] == 0 and type(fire[x][y])==int): continue
            if not fire[x][y] or fire[x][y] > fire[cur[0]][cur[1]]+1:
                fire[x][y] = fire[cur[0]][cur[1]]+1
                que.append((x,y))
    return False
    
for i in range(R):
    for j in range(C):
        if miro[i][j] == 'F':
            que.append((i,j))
            fire[i][j] = 0
        elif miro[i][j] == 'J':
            jh = (i,j)
            fire[i][j] = 0
bfs()
cur = esc()
if cur:
    print(fire[cur[0]][cur[1]]+1)
else:
    print('IMPOSSIBLE')




    
