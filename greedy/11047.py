'''
동전 0
동전의 종류 N
가치의 합 K
'''
n, k = map(int, input().split())
# 동전의 가치가 오름차순으로 주어짐
count = 0
price = [int(input()) for _ in range(n)]
for p in range(n-1, -1,-1):
    if k//price[p] > 0:
        c = k//price[p] # 최대 동전의 수
        k-= price[p]*c
        count+=c
print(count)
