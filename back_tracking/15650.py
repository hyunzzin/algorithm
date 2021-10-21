# 1부터 N까지 중복 없이 M개를 고른 수열
# permutation, 순열에 관한 문제이다.
n, m = map(int, input().split())
arr = [0]*(m+1)

def permutation(x):
    if x == m+1:
        for i in range(1, m+1):
            print(arr[i], end = ' ')
        print() # 줄바꿈인가
    else:
        for i in range(1, n+1):
            if max(arr) < i:
                arr[x] = i
                permutation(x+1)
                arr[x] = 0

permutation(1)
    
# 중복이 핵심, 중복을 방지하기 위해 visit의 인덱스로 사용된 숫자를 표시
'''
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

