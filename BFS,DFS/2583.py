'''
영역 구하기
직사각형이 전체를 채우는 경우는 없다

출력
1. 분리되어 나누어지는 영역의 개수
2. 각 영역의 넓이를 오름차순으로 정렬

5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''h
import sys
from collections import deque

M,N,K = map(int, sys.stdin.readline().split())
arrK=[]
for _ in range(K):
    arrK.append(list(map(int,sys.stdin.readline().split())))
    # 왼쪽 아래 꼭짓점 좌표, 오른쪽 위의 꼭짓점 좌표
    
