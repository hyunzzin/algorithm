'''
N과 M
1부터 N까지 중복 없이 M개를 고른 수열
오름차순
'''
# 1번째 풀이

n, m = map(int, input().split())
arr = [0] * (m + 1)


def permutation(x):
    if x == m + 1:
        for i in range(1, m + 1):
            print(arr[i], end=" ")
        print()  # 줄바꿈인가
    else:
        for i in range(1, n + 1):
            if max(arr) < i:
                arr[x] = i
                permutation(x + 1)
                arr[x] = 0
permutation(1)


# 2번째 풀이
import sys
n,m = map(int, sys.stdin.readline().split())
visited = [False for _ in range(n+1)] # 방문 여부 확인
arr = [False for _ in range(m)] # m의 개수만큼 수 저장
def bt(cnt,k):
    if cnt == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(k, n+1):
        if not visited[i]:
            visited[i] = True
            arr[cnt] = i
            bt(cnt+1,i)
            visited[i] = False
bt(0,1)
