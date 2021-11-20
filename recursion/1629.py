'''
곱셈
자연수 A를 B번 곱한 수에 C를 나눈 나머지
'''
import sys
a,b,c = map(int, sys.stdin.readline().split())

def pow(a,b,c):
    if b == 1:
        return a%c
    val = pow(a,b//2,c)
    val = val*val %c # 나머지가 c보다 더 커졌을 때 c로 나눈 나머지를 한번 더 구해준다.
    if b%2 == 0: # b가 짝수인 경우
        return val
    return val*a%c # b가 홀수인 경우

print(pow(a,b,c))
