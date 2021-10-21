'''
무한대일때
r1 = r2 and 좌표 같을때(d=0)

2개일 때
r2 - r1 < d < r1+r2

1개일 때
r1+r2 = d
r2-r1 = d

0개일 때
d > r1 + r2
r2-r1 > d
d = 0

'''
count = int(input())
for i in range(count):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = (pow(x2-x1, 2)+pow(y2-y1, 2))**0.5

    if r1 == r2 and d == 0:
        print(-1)
    elif abs(r2-r1) < d and d < r1+r2:
        print(2)
    elif r1+r2 == d or abs(r2-r1)==d:
        print(1)
    elif d > r1+r2 or abs(r2-r1) > d or d == 0:
        print(0)
