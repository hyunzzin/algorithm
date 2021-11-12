'''
다리 만들기
3:23
한 섬과 다른 섬을 잇는 다리 하나
다리를 가장 짧게 만든다.
육지 : 1
바다 : 0
섬은 항상 두개 이상

'''
import sys
from collections import deque
country=[]
vis_check = [[False for _ in range(100)] for _ in range(100)]
n = int(sys.stdin.readline())
for _ in range(n):
    country.append(list(map(int, sys.stdin.readline().split())))

'''
가장 거리가 가까운 섬을 구하기
가장 짧은 다리 놓기
간척사업을 한다.
상하좌우에 바다가 아니라 섬이 있다면 출력,빠져나오기
1. 섬찾기 ( 섬이 총 몇개인지)
2. 섬마다 다른 숫자로 바꿔주기 -1, -2 등
3. 섬 가장자리만 que에 넣어주기
4. 섬 가장자리에서부터 자신의 땅을 넓혀나간다.
5. 섬을 넓히고 옆 에 다른 섬이 있다면 그 수 반환
6. 상하좌우에 있는지 검사하려면 방문 배열이 따로 있어야 한다.
'''
island_cnt = 0
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 섬 가장자리 que와 섬을 구별할 넘버
bound = deque()
num = 0
# 섬마다 다른 숫자로 바꿔주기
for i in range(n):
    for j in range(n):
        if vis_check[i][j] or not country[i][j]: continue
        island_cnt+=1
        q.append((i,j))
        num-=1
        country[i][j] = num
        

        # 섬 시작
        while q:
            cur = q.popleft()
            for k in range(4):
                x = cur[0] + dx[k]
                y = cur[1] + dy[k]
                if x < 0 or x>= n or y < 0 or y >= n: continue
                if vis_check[x][y]: continue
                if not country[x][y]: # 다음 부분이 가장자리면
                    bound.append((cur[0],cur[1]))
                else:
                    q.append((x,y))
                    country[x][y] = num
                    vis_check[x][y] = True

brid = 0
ans = sys.maxsize
while bound :
    brid+=1
    for _ in range(len(bound)):
        cur = bound.popleft()
        for k in range(4):
            x = cur[0] +dx[k]
            y = cur[1] +dy[k]
            if x < 0 or x>= n or y < 0 or y >= n: continue
            if country[x][y] == country[cur[0]][cur[1]]: continue
            if not country[x][y]: # 가장자리면서 바다이면
                country[x][y] = country[cur[0]][cur[1]]
                bound.append((x,y))
                
            elif country[x][y] < country[cur[0]][cur[1]]:
                ans = min(ans,(brid-1)*2)
            elif country[x][y] > country[cur[0]][cur[1]]:
                ans = min(ans,brid*2-1)
print(ans)














            
