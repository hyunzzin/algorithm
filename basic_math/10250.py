import math

count = int(input())
for i in range(count):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(h * 100 + math.ceil(n / h))
    else:
        print(n % h * 100 + math.ceil(n / h))


"""
T=int(input())
for i in range(T):
    H, W, N= map(int, input().split())
    print(((N-1)%H+1)*100+(N-1)//H+1)
"""
