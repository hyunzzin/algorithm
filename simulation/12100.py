'''
5번 이동의 경우의 수 1024개
블록을 합치는 방법
    같은 숫자여야 하고 한번 계산한 블록은 두번 계산할 수 없다.
    first = 더할 블록
    maxN = 순회안했을 경우 제일 큰 숫자
    순서 index = 0
    순회 중
        first가 있다면
            first와 같다면
                first와 더한다. 본인만 초기화,  max와 비교한다.
            first가 다르다면
                first에 대입하고 그 자리는 초기화한다.
            first는 index 위치에 삽입해주고 index+=1
        first가 없다면
            first에 대입하고 그 자리는 초기화한다.
    순회가 끝난 후
    first가 있다면
        index에 삽입
        max와 비교한다.
    
블록의 이동
위 - (0,y)(0,x)
아래 - (0,y)(x-1,-1,-1)
오른쪽 - (0,x)(y-1,-1,-1)
왼쪽 - (0,x)(0,y)

테스트 케이스
https://www.acmicpc.net/board/view/16151

'''
def move(arr,q,n):
    maxN = -sys.maxsize
    if q == 0 or q==1:
        mx = [(0,n,1),(n-1,-1,-1)]
        for i in range(n):
            first = 0 # 더할 블록
            idx = mx[q][0]
            for j in range(mx[q][0],mx[q][1],mx[q][2]):
                #print('j',j,'i',i)
                if first:
                    if first == arr[j][i]:
                        first += arr[j][i]
                        arr[j][i] = 0
                        #print('1',idx,i)
                        arr[idx][i] = first
                        first = 0
                        maxN = max(maxN,first)
                    else:
                        maxN = max(maxN,first)
                        #print('2',idx,i)
                        arr[idx][i] = first
                        first = arr[j][i]
                        arr[j][i] = 0
                    if q==0:
                        idx+=1
                    else:
                        idx-=1
                else:
                    #print('no first',first)
                    first = arr[j][i]
                    arr[j][i] = 0
            if first:
                arr[idx][i] = first
                maxN = max(maxN,first)
            #print(j,i)    
    elif q == 2 or q==3:
        my = [0,0,(n-1,-1,-1),(0,n,1)]
        for i in range(n):
            first = 0 # 더할 블록
            idx = my[q][0]
            for j in range(my[q][0],my[q][1],my[q][2]):
                if first:
                    if first == arr[i][j]:
                        first += arr[i][j]
                        arr[i][j] = 0
                        arr[i][idx] = first
                        first = 0
                        maxN = max(maxN,first)
                    else:
                        maxN = max(maxN,first)
                        arr[i][idx] = first
                        first = arr[i][j]
                        arr[i][j] = 0      
                    if q==2:
                        idx-=1
                    else:
                        idx+=1
                else:
                    first = arr[i][j]
                    arr[i][j] = 0
            if first:
                arr[i][idx] = first
                maxN = max(maxN,first)
    return arr,maxN
    

# 상하좌우 경우의 수
def case(num,c,cases,q,arr,n):
    global ans
    if num == c:
        arr_c = copy.deepcopy(arr)
        #print(q)
        for j in range(5):
            arr_c,max_n = move(arr_c,q[j],n)
        ans = max(ans,max_n)
        #print(maxN)
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






















