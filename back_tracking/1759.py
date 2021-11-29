'''
암호 만들기
알파벳이 증가하는 순서로 배열 k필요
중복 안되니까 visited도 필요
l개의 암호문자와 c개의 문자 (최소 한개의 모음과 두개의 자음)
1. 오름차순 정렬한다.

함수 정의
    def(n,k,m,j)
base condition
    if n == l:
        if seq[i] in ['a','e','i','o','u']:
            print()
        return 
재귀 식
    def(n+1,k,m,j)
'''
import sys
l,c = map(int, sys.stdin.readline().split())
seq = sorted(list(sys.stdin.readline().split()))
visited = [False for _ in range(c)]
arr = [False for _ in range(l)]
def bt(n,k,m,j):
    if n == l:
        if m >=1 and j >=2:
            print(''.join(map(str,arr)))
        return
    
    for i in range(k,c):
        if not visited[i]:
            if seq[i] in ['a','e','i','o','u']:
                m+=1
            else:
                j+=1
            visited[i]=True
            arr[n] = seq[i]
            bt(n+1,i,m,j)
            visited[i]=False
            if seq[i] in ['a','e','i','o','u']:
                m-=1
            else:
                j-=1
    
bt(0,0,0,0)        
