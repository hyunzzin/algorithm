'''
m, n = map(int, input().split())
def decArr(n):
    dec = [2]
    dec += list(range(3,n+1,2)) 
    # print(dec)
    square = int(n ** 0.5)
    i = 0
    while dec[i] <= square:
        count = n//dec[i]
        for j in range(2,count+1):
            if (dec[i]* j) in dec:
                dec.remove(dec[i]* j)
        i+=1
    return dec

dec = decArr(n)
#print(dec)

for i in dec:
    if i >= m:
        print(i)



m, n = map(int, input().split())
dec = [2]
dec += list(range(3,n+1,2)) 
# print(dec)
square = int(n ** 0.5)
i = 0
while dec[i] <= square:
    count = n//dec[i]
    for j in range(2,count+1):
        if (dec[i]* j) in dec:
            dec.remove(dec[i]* j)
    i+=1
    
for i in dec:
    if i >= m:
        print(i)
# in(하나하나 순회, 데이터 크기만큼의 시간복잡도를 가짐)과
# remove(하나하나 순회, 데이터 크기만큼의 시간복잡도를 가짐)가 시간초과의 원인


내 코드 중 비교 코드
M,N = map(int, input().split())
for i in range(M, N+1):
    N = i
    div = 2
    square = int(N ** 0.5)
    while div <= square:
        if N%div != 0:
            div+=1
        else:
            # print(div)
            N //= div
    if N != 1 and N == i:
        print(N)

# 여기서 굳이 소인수분해과정에서 소인수가 1과 자신 이외에 다른 수가 있다는 것을
# 알아버린 순간 반복문을 빠져나와야 했다.

다른 답
#1929번

import sys

m, n = map(int, sys.stdin.readline().split())

def sosu(m, n):

    n += 1
    data = [True] * n

    for i in range(2, int(n**0.5)+1):
        if data[i]:
            for j in range(2*i, n, i):
                data[j] = False

    for i in range(m, n):
        if data[i]==True and i>1:
            print(i)
   
sosu(m, n)


내 정답 코드
- 소인수가 1과 자신뿐이면 소수
def isPrime(num):
    if num == 1:
        return False
    i = num
    for div in range(2,int(num ** 0.5)+1):
        if num%div == 0:
            return False
    return True

M,N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)

메모리는 제일 적게 사용하지만 시간이 오래걸림

        
'''
# True로 배열을 채우는게 숫자로 채우는 것보다 메모리, 시간에서 차이남
m, n = map(int, input().split())
def decArr(n):
    dec = [True]*(n+1)
    square = int(n ** 0.5)
    i = 2
    while i <= square:
        count = n//i
        if bool(dec[i]):
            for j in range(2,count+1):
                dec[i*j] = False
        i+=1
    return dec

dec = decArr(n)
#print(dec)

for i in range(m,n+1):
    if i > 1 and dec[i]:
        print(i)


