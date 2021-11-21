'''
하노이 탑
n-1개의 원판을 기둥 1에서 기둥 2로 옮긴다.
n번 원판을 기둥 1에서 기둥 3으로 옮긴다.
n-1개의 원판을 기둥 2에서 기둥 3으로 옮긴다.
-> 원판이 n-1개일 때 옮길 수 있으면 원판이 n개일 때에도 옮길 수 있다.
1. 함수의 정의
    def a,b,n: 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력하는 함
2. base condition
    n=1일 때 a에서 b로 이동
3. 재귀 식
'''
n = int(input())
def hanoi(from_,by_,to_,n):
    if n==1:
        print(from_,to_)
        return 
    hanoi(from_,to_,by_,n-1)
    print(from_,to_)
    hanoi(by_,from_,to_,n-1)
    return 

print(2**n-1)
hanoi('1','2','3',n)
