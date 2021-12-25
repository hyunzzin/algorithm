'''
치킨 배달
0 : 빈칸
1 : 집
2 : 치킨집
도시의 칸 (r,c)
거리 abs(r1-r2) + abs(c1-c2)
출력 : m개의 치킨집을 폐업시키지 않았을 때 도시의 치킨 거리의 최솟값
도시의 치킨 거리 : 모든 집의 치킨 거리의 합


1. m개의 치킨집 좌표 경우의 수 구하기
2. 집에서 가까운 치킨집과의 치킨거리 구하기 -> 다 더해서 모든 집의 치킨 거리의 합을 구한다.
3. 그 중에서 가장 작은 치킨거리 값 구하기

'''
import sys
from itertools import combinations
input = sys.stdin.readline

n,m=map(int, input().split())
maps=[]
for i in range(n):
  maps.append(list(map(int, input().split())))

home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            home.append((i,j))
        elif maps[i][j]==2:
            chicken.append((i,j))

pick_chicken=list(combinations(chicken,m)) # chicken에서 모든 조합을 계산 (중복x)
result=[0]*len(pick_chicken)
ans = sys.maxsize

for i in home: # 각 집에서
    for j in range(len(pick_chicken)): #치킨집 경우의 수만큼
        sumN=0
        tmp = sys.maxsize
        for k in pick_chicken[j]: # 치킨거리 합 구하기
            dis=abs(i[0]-k[0])+abs(i[1]-k[1])
            tmp=min(tmp,dis)
        result[j]+=tmp
    
print(min(result))










