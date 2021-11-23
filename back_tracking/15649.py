'''
N과 M
1부터 N까지 중복 없이 M개를 고른 수열
permutation, 순열에 관한 문제이다.
수를 하나씩 추가하면서 길이가 M인 수열이 완성되면 출력

백트래킹 문제의 코드 구조
def 재귀함수(x):
    if 정답이라면?:
        정답 출력 또는 저장 등
    else: 정답이 아니라면?
        for 뻗을 수 있는 모든 자식 노드에 대해서 :
            if 정답에 유망하다면:
                자식노드로 이동
                재귀함수(x+1)
                부모노드로 이동

'''

import sys
n,m = map(int, sys.stdin.readline().split())
# 수열을 담을 배열
arr= [False for _ in range(m)]
# 특정 수가 쓰였는지 true or false로 나타내는 배열
visited = [False for _ in range(n+2)]


def bt(k):
    if k == m: # 개수를 다 골랐다면
        for i in range(m):
            print(arr[i],end=' ') # 수열 출력하기 m이 2면 1 2이렇게 출력된다.
        print()
        return
    for i in range(1,n+1): # 1부터 n까지 m개를 고르는 것
        if not visited[i]: # 특정 수가 사용되지 않았다면
            arr[k] = i
            visited[i]=1
            bt(k+1) # 출력되고 나면 다시 방문안한 상태로 돌려주기
            visited[i]=0

bt(0)

























