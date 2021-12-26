import sys
from collections import deque
input = sys.stdin.readline
'''
왼쪽 톱니는 2번째 / 오른쪽 톱니는 6번째
극이 다르면 반대로 회전
극이 같으면 회전X
'''
def solution():
    arr = []
    for _ in range(4):
        arr.append(deque(list(map(int,input().strip('\n')))))
    spin = int(input()) # 회전횟수
    for _ in range(spin):
        rotate_st = [False,False,False,False] # 톱니 회전 여부
        order = [False,False,False,False] # 회전 방향
        num,spin_direc = map(int, input().split())

        stack = [num-1]
        order[num-1] = spin_direc
        rotate_st[num-1]=True
        while stack:
            cur = stack.pop()
            # 톱니를 회전하기 전에 회전 방향 구하기
            for i in [1,-1]:
                if cur+i<0 or cur+i>3: continue
                if rotate_st[cur+i]: continue
                if i==1: # 오른쪽 톱니
                    if arr[cur][2] != arr[cur+i][6]: # 오른쪽 톱니와 다르면
                        order[cur+i] = order[cur]*(-1)
                    else: # 같으면
                        order[cur+i]=0
                elif i==-1: # 왼쪽 톱니
                    if arr[cur][6] != arr[cur+i][2]: # 오른쪽 톱니와 다르면
                        order[cur+i] = order[cur]*(-1)
                    else: # 같으면
                        order[cur+i]=0
                rotate_st[cur+i]=True
                stack.append(cur+i)
        # 회전하기
        for k in range(4):
            arr[k].rotate(order[k])
    return arr[0][0]*1 + arr[1][0]*2 + arr[2][0]*4 + arr[3][0]*8
print(solution())

















