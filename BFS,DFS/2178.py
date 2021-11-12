'''
BFS
O(NM)
스택에 첫번째 좌표 넣기
좌표가 범위를 벗어나면 안된다. -> 예외처리
칸마다 거리를 저장(vis_check에) - 시작점과의 거리를 잰다.
다 방문하면 마지막 배열 값을 반환
미로가 0이거나 방문해서 true값이면 건너뛰기
상하좌우를 계산해서 방문배열에 저장 

'''
import sys
from collections import deque
miro = []
vis_check=[[False for m in range(100)] for _ in range(100)]
vis_check[0][0] = 1
N,M = map(int, sys.stdin.readline().split())
for _ in range(N):
    miro.append(list(sys.stdin.readline().strip('\n')))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
stack = deque([(0,0)])

while True:
    cur = stack.popleft()
    if cur[0] == N-1 and cur[1] == M-1:
        break
    for i in range(4):
        x = cur[0] + dx[i]
        y = cur[1] + dy[i]
        if x >= N or x < 0 or y >= M or y < 0: continue
        if miro[x][y] == '0' or vis_check[x][y] > 0: continue
        vis_check[x][y] = vis_check[cur[0]][cur[1]]+1
        stack.append((x,y))

print(vis_check[N-1][M-1])









        
        
