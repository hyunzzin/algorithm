'''
N과 M(6)
함수 정의
    def(cnt, k)
base condition
    if cnt == m:
        print()
        return
재귀 식
    def(cnt+1,i)
'''
import sys
n,m = map(int, sys.stdin.readline().split())
seq=sorted(list(map(int,sys.stdin.readline().split())))
visited = [False for _ in range(n)]
arr = [False for _ in range(m)]

def bt(cnt, k):
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(k,n):
        if not visited[i]:
            arr[cnt] = seq[i]
            visited[i]=True
            bt(cnt+1, i)
            visited[i] = False
            
bt(0,0)
