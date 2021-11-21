'''
Z
1. 함수의 정의
    def Z(n,r,c)
    2^n x 2^n 배열에서 (r,c)를 방문하는 순서를 반환하는 함수
2. base condition
    n=0일 때 return 0
3. 재귀 식
    사각형이 속한 구역으로 나눌 것
    1번 사각형일 때 return def(n-1, r, c)
    2번 사각형일 때 return half*half + def(n-1, r, c-half)
    3번 사각형일 때 return 2*half*half + func(n-1, r-half, c)
    4번 사각형일 때 return 3*half*half + func(n-1, r-half, c-half)
'''
import sys
n,r,c = map(int, sys.stdin.readline().split())

def Z(n,r,c):
    
    return
Z(n,r,c)
