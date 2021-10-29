"""
작은 수부터 출력
"""


def Prime(n):
    dec = [True] * (n + 1)
    square = int(n ** 0.5)
    for i in range(2, square + 1):
        count = n // i
        if dec[i]:
            for j in range(2, count + 1):
                dec[i * j] = False
    return dec


dec = Prime(10000)

count = int(input())
for i in range(count):
    N = int(input())
    minN = N // 2
    maxN = N // 2
    for j in range(minN, 1, -1):
        if dec[j] and dec[maxN]:
            print(j, maxN)
            break
        maxN += 1
