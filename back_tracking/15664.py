'''
N과 M(10)
함수 정의
    def(cnt, k)
base condition
    if cnt == m:
        print()
        return
재귀 식
    def(cnt+1, i)
'''
import sys
n,m = map(int, sys.stdin.readline().split())
seq = sorted(list(map(int, sys.stdin.readline().split())))
arr = [False for _ in range(m)]
visited = [False for _ in range(n)]

def bt(cnt,k):
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    visit = 0
    for i in range(k,n):
        if not visited[i] and visit != seq[i]:
            visited[i] = True
            arr[cnt] = seq[i]
            visit = seq[i]
            bt(cnt+1,i)
            visited[i] = False

bt(0,0)
