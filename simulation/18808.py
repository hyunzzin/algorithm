import sys, copy
input = sys.stdin.readline
N,M,K = map(int, input().split())
note = [[0 for _ in range(M)]for _ in range(N)]
def stick(start,r,c,sticker,flag):
    x,y = start
    for i in range(r):
        for j in range(c):
            if flag:
                if not note[x+i][y+j]:
                    note[x+i][y+j] = sticker[i][j]
            else:
                # 스티커 있는 자리에 스티커 붙이려고 하면
                if sticker[i][j] and note[x+i][y+j]:
                    return False
    return True

def rotation(r,c,sticker):
    new_st = [[0 for _ in range(r)]for _ in range(c)]
    for j in range(c):
        for i in range(r-1,-1,-1):
            new_st[j][r-1-i]= sticker[i][j]
    return new_st

# 스티커 개수만큼 반복
for _ in range(K):
    # 스티커 입력받기
    R,C = map(int, input().split())
    sticker = []
    for _ in range(R):
        sticker.append(list(map(int, input().split())))
    # 스티커가 너무 크면 못붙임
    if (N<R and N<C) or (M<R and M<C):
        continue
    # 스티커가 가로만 튀어나오면 회전
    if N<R or M<C:
        sticker=rotation(R,C,sticker)
        R,C=C,R
    
    flag = False
    for _ in range(4):
        if flag: break
        # 시작점 찾기
        start = (0,0)
        for x in range(N):
            for y in range(M):
                if N-x<R or M-y<C:
                    break
                start = (x,y)
                # 스티커 붙임
                flag = stick(start,R,C,sticker,flag)
                if flag:
                    stick(start,R,C,sticker,flag)
                    break
            if flag:
                break
        # 다 안붙으면 스티커를 회전
        if not flag:
            sticker = rotation(R,C,sticker)
            R,C=C,R
ans = 0
for c in note:
    ans += c.count(1)
print(ans)
