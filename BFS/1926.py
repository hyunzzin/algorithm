
'''
이중 for 문을 사용해서 그림이 끊어져도 다른 시작점 찾기

빨간 칸, 방문한 칸을 거르고 그림칸, 즉 1이 나오면 반복하기
(시작점은 무조건 방문했다고 표시해준다!!!)

그림의 개수(1로 된 것들)와 넓이가 가장 넓은 것의 넓이를 구하기
    - 배열에 넣고 len과 max를 구하기
'''
import sys
from collections import deque
visit_check = [[False for _ in range(500)] for _ in range(500)]

C, R = map(int, sys.stdin.readline().split())
pic = []
for _ in range(C):
    pic.append(list(map(int, sys.stdin.readline().split())))
cnt = 0 # 그림의 수
mx = 0 # 그림의 최댓값
dx = [1,0,-1,0] # 하우상좌
dy = [0,1,0,-1]
re = []
for c in range(C):
    for r in range(R):
        if not pic[c][r] or visit_check[c][r]: # 그림이 없거나 방문했으면 넘어간다.
            continue
        cnt+=1
        q = deque([(c,r)]) # 큐 선언
        visit_check[c][r] = True
        area = 0
        while q: # 큐에 남아있으면
            area += 1 # 넓이 증가
            cur = q.popleft()
            for i in range(4):
                x = cur[0] + dx[i] 
                y = cur[1] + dy[i]
                if(x < 0 or x >= C or y < 0 or y >= R): continue # 그림의 범위에 벗어나는 애들
                if visit_check[x][y] or not pic[x][y]: continue # 방문한 칸이거나 파란칸이 아닌 경우
                visit_check[x][y] = True
                q.append((x,y)) # 큐에 넣기
                
        mx = max(area, mx) # 제일 넓은 도형 저장
print(cnt)
print(mx)




