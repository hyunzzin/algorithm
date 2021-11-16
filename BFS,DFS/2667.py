import sys
from collections import deque

n = int(sys.stdin.readline())
apart = []
for _ in range(n):
    apart.append(list(map(int, sys.stdin.readline().strip('\n'))))

visited = [[False for _ in range(n)]for _ in range(n)]

def BFS():
    cnt = 0
    que = deque()
    all_area = []
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(n):
        for j in range(n):
            if visited[i][j] or not apart[i][j]: continue
            visited[i][j] = True
            que.append((i,j))
            cnt+=1
            area = 1
            while que:
                cur = que.popleft()
                for k in range(4):
                    x = cur[0]+dx[k]
                    y = cur[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n:continue
                    if visited[x][y] or not apart[x][y]: continue
                    que.append((x,y))
                    visited[x][y]=True
                    area+=1
            all_area.append(area)
                
    return cnt,sorted(all_area)

ans_cnt, ans_area =BFS()
print(ans_cnt)
for a in ans_area:
    print(a)
