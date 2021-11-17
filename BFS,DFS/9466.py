'''
텀 프로젝트
프로젝트 팀원 수에는 제한이 없음
모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택(단, 한명만 선택 가능)
자기 자신 선택 가능
어느 팀에도 속하지 않는 학생들의 수 1:58
'''
import sys
sys.setrecursionlimit(10**8)
T = int(sys.stdin.readline().strip('\n'))

def DFS(i, cnt):
    nxt_num = choice[i]
    vis_check[i] = True

    if not vis_check[nxt_num]:
        cnt = DFS(nxt_num, cnt)
    else:
        if not Done[nxt_num]:
            j = nxt_num
            while j != i:
                j = choice[j]
                cnt+=1
                
            cnt+=1
    Done[i] = True
    return cnt

for _ in range(T):
    stu = int(sys.stdin.readline())
    vis_check = [False for _ in range(stu+2)]
    Done = [False for _ in range(stu+2)]
    choice = [0]+list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(1,stu+1):
        if not vis_check[i]:
            
            cnt = DFS(i, cnt)

    print(stu-cnt)
