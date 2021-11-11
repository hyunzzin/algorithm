'''
안전영역

O(N)이 최대 100만
'''
import sys
from collections import deque
n = int(sys.stdin.readline())
area = []
ans = 1 # 안전한 영역 중 최대
bottom = sys.maxsize
top = -1
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    area.append(temp)
    bottom = min(min(temp),bottom)
    top = max(max(temp),top)
    

def BFS(h):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    que = deque()
    cnt=0
    visited = [[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] or area[i][j]<=h: continue
            que.append((i,j))
            visited[i][j]=True
            cnt+=1
            while que:
                cur = que.popleft()
                for k in range(4):
                    x = cur[0]+dx[k]
                    y = cur[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n:continue
                    if visited[x][y] or area[x][y]<=h:continue
                    que.append((x,y))
                    visited[x][y]=True
    return cnt


for h in range(bottom,top+1):
    ans=max(ans, BFS(h))

print(ans)
