'''
정리
https://brillistar.tistory.com/3
'''
def move(arr_c,q,n):
    maxN = -sys.maxsize
    # 위쪽, 아래쪽 이동
    if q == 0 or q==1: 
        mx = [(0,n,1),(n-1,-1,-1)]
        for i in range(n):
            first = 0 # 더할 블록
            idx = mx[q][0]
            for j in range(mx[q][0],mx[q][1],mx[q][2]):
                # 0일 경우 건너뛰기
                if arr_c[j][i]==0: continue
                
                # first가 있다면
                if first: 
                    if first == arr_c[j][i]: # first와 수가 같다면
                        first += arr_c[j][i]
                        arr_c[j][i] = 0
                        arr_c[idx][i] = first
                        maxN = max(maxN,first)
                        first = 0
                        
                    else: # first와 수가 다르다면
                        maxN = max(maxN,first)
                        arr_c[idx][i] = first
                        first = arr_c[j][i]
                        arr_c[j][i] = 0
                        
                    if q==0: # 위쪽 이동이면
                        idx+=1
                    else: # 아래쪽 이동이면
                        idx-=1
                        
                # first가 없다면
                else:
                    first = arr_c[j][i]
                    arr_c[j][i] = 0
            if first:
                arr_c[idx][i] = first
                maxN = max(maxN,first)
                
    # 오른쪽, 왼쪽 이동
    elif q == 2 or q==3: 
        my = [0,0,(n-1,-1,-1),(0,n,1)]
        for i in range(n):
            first = 0 # 더할 블록
            idx = my[q][0]
            for j in range(my[q][0],my[q][1],my[q][2]):
                # 0일 경우 건너뛰기
                if arr_c[i][j]==0: continue
                
                # first가 있다면
                if first:
                    if first == arr_c[i][j]: # first와 수가 같다면
                        first += arr_c[i][j]
                        arr_c[i][j] = 0
                        arr_c[i][idx] = first
                        maxN = max(maxN,first)
                        first = 0
                        
                    else: # first와 수가 다르다면
                        maxN = max(maxN,first)
                        arr_c[i][idx] = first
                        first = arr_c[i][j]
                        arr_c[i][j] = 0
                        
                    if q==2: # 오른쪽 이동이면
                        idx-=1
                    else: # 왼쪽 이동이면
                        idx+=1

                # first가 없다면
                else:
                    first = arr_c[i][j]
                    arr_c[i][j] = 0
            if first:
                arr_c[i][idx] = first
                maxN = max(maxN,first)
    return arr_c,maxN
    

# 상하좌우 경우의 수
def case(num,c,cases,q,arr,n):
    global ans
    if num == c:
        arr_c = copy.deepcopy(arr)
        for j in range(5):
            arr_c,max_n = move(arr_c,q[j],n)
        ans = max(ans,max_n)
        return
    
    for i in range(4):
        q[num] = cases[i]
        case(num+1,c,cases,q,arr,n)



def solution(n,arr):
    global ans
    ans = 0
    q = [0,0,0,0,0]
    cases = [0,1,2,3]
    case(0,5,cases,q,arr,n)
    print(ans)
    return

import sys,copy
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
solution(n,arr)






















