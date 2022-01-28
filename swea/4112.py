import sys
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b = map(int, input().split())
    if a==b:
        print(test_case, 0)
        continue
    s =max(a,b)
    st,ed = 0,0
    pira = []
    n = 1
    # 피라미드 만들기
    for i in range(1,s+1):
        if i == ((n-1)*n//2+1):
            pira.append([0])
            n+=1
        else:
            pira[-1].append(0)
        if i == a:
            st = (len(pira)-1,len(pira[-1])-1)
        elif i == b:
            ed = (len(pira)-1,len(pira[-1])-1)

    dx = [1,-1,0,0,1,-1]
    dy = [0,0,1,-1,1,-1]
    q = deque([st])
    pira[st[0]][st[1]]=0
    while q:
        cx,cy = q.popleft()
        if cx == ed[0] and cy == ed[1]:
            break
        for k in range(6):
            x = cx+dx[k]
            y = cy+dy[k]
            if x<0 or y<0 or x>=len(pira) or y>=len(pira[x]): continue
            if pira[x][y] >0: continue
            q.append((x,y))
            pira[x][y]= pira[cx][cy]+1
    print(test_case, pira[cx][cy])      
    
