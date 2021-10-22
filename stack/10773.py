'''
재현 : 잘못된 수를 부를 때마다 0을 외침, 최근에 재민이가 쓴 수를 지우게 시킴
재민 : 모든 수의 합을 알고 싶음

1<= K <= 100,000
k개의 수는 모두 정수(n)이며 0< n <1,000,000
'''
k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))
