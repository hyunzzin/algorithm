def Prime(n):
    dec = [True]*(n+1)
    square = int(n ** 0.5)
    for i in range(2,square+1):
        count = n//i
        if bool(dec[i]):
            for j in range(2,count+1):
                dec[i*j] = False
    return dec
dec = Prime(123456*2)
M = 1
while M != 0:
    M = int(input())
    if M == 0: break
    N = 2*M
    print(dec[M+1:N+1].count(True))
