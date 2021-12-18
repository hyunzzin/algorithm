'''
BFS
사각형마다 시작점 +a
BFS해서 전부 같은 숫자인지 확인할 수 있는 함수
시작점, 길이 구분하기
출력 [0의 개수, 1의 개수]
'''
from collections import deque
def solution(arr):
    ans = []
    bfs(0,0,arr,ans)
    #print(ans)
    answer = []
    return [ans.count(0),ans.count(1)]
# 전부 같은 숫자인지 확인
'''
0,0 0,2 
2,0 2,2
'''
def bfs(x,y,arr,ans):
    q = deque([(0,0,len(arr))])
    while q:
        cx,cy,l = q.popleft()
        tmp = check(cx,cy,l,arr)
        if tmp > -1:
            ans.append(tmp)
        else:
            # 쪼개기
            l_div = l//2
            q.append((cx,cy,l_div))
            q.append((cx,cy+l_div,l_div))
            q.append((cx+l_div,cy,l_div))
            q.append((cx+l_div,cy+l_div,l_div))
        
    '''
    같은 숫자면 숫자 ans에 넣기
    다르면 쪼개기 -> q에 좌표 4개 넣기
    '''
    return
def check(x,y,l,arr): # -1 / 0,1 반환
    num = arr[x][y]
    for i in range(x,x+l):
        for j in range(y,y+l):
            if num != arr[i][j]:
                return -1
    return num
