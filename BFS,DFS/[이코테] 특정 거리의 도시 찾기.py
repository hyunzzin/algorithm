'''
특정 거리의 도시 찾기
최단거리가 K인 도시
'''
import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split())
visited = [False for _ in range(n+1)] # 방문했는지 저장
print(visited)
visited[x] = True
road = [[] for _ in range(n+1)] # 단방향 입력 저장
result = []
for _ in range(m):
    i,j = map(int,input().split())
    road[i].append(j)
print(road)
q = deque([(x,0)]) # 출발지와 distance 저장
while q:
    print(q)
    st, dis = q.popleft()
    if dis == k:
        result.append(st)
    elif dis < k:
        for r in road[st]:
            if not visited[r]:
                visited[r] = True
                q.append((r, dis+1))
if not result:
    print(-1)
else:
    result.sort()
    for ans in result:
        print(ans)
        

