'''
N-Queen

'''
import sys
n = int(sys.stdin.readline())
# 각 대각선과 열의 점유 상태를 나타낼 visited 변수
visited1 = [False for _ in range(n)]
visited2 = [False for _ in range(2*n-1)]
visited3 = [False for _ in range(2*n-1)]
def queen(cur,cnt):
    if cur == n:
        cnt+=1
        return cnt
    # i는 y
    for i in range(n):
        if visited1[i] or visited2[cur+i] or visited3[cur-i+n-1]:# 방문 했으면
            continue
            # 계속해서 다음 수를 찾는다.
        # visited에 들어갈 수 있으면 visitied를 1로 바꾼다.
        visited1[i] = 1
        visited2[cur+i] = 1
        visited3[cur-i+n-1] = 1
        cnt = queen(cur+1,cnt)
        visited1[i] = 0
        visited2[cur+i] = 0
        visited3[cur-i+n-1] = 0
        # 재귀
    return cnt
print(queen(0,0))
