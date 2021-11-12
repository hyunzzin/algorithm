'''
텀 프로젝트
프로젝트 팀원 수에는 제한이 없음
모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택(단, 한명만 선택 가능)
자기 자신 선택 가능
어느 팀에도 속하지 않는 학생들의 수 1:58
'''
import sys
from collections import deque
vis_check = [False for _ in range(100002)]
Done = [False for _ in range(100002)]
T = int(sys.stdin.readline())
for _ in range(T):
    stu = int(sys.stdin.readline())
    choice = list(map(int, sys.stdin.readline().split()))
    # 자기 자신을 선택하는 경우
    # 다른 사람을 선택하는 경우
    cnt = 0
    for i in range(stu):
        if not vis_check[i]:
            DFS()
            
        
    

def BFS():
    if visit_check[]

