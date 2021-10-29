"""
1. 세 정수 입력받기
2. 달팽이가 나무를 모두 올라가는데 걸리는 시간인 변수 day 생성
3. 달팽이의 현재 위치를 나타내는 변수 m 생성
3. 달팽이가 정상을 올라갈때까지 반복
    - 정상에 올라갔는지 확인
        - 정상 이상이라면 반복문 탈출
        - 정상 이하라면 미끄러져 내려오기, day+1
"""
import math

a, b, v = map(int, input().split())

x = math.ceil((v - a) / (a - b) + 1)

print(x)
"""
a, b, v = map(int,input().split())
if v%(a-b) != 0:
    print(v//(a-b)+1)
else:
    print((v//(a-b)) - (a//(a-b)) +1)
"""
