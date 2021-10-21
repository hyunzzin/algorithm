n = int(input())

def decom(n):
    lenN= len(str(n))
    start = n-lenN*9
    if n-lenN*9 < 18:
        start = 0
    for i in range(start, n):
        sumI = 0
        for j in str(i):
            sumI+=int(j)
        if i+sumI == n:
            return i
    return 0

print(decom(n))
        
