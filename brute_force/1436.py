n = int(input())
def number(n):
    count = 1
    num = 666
    while count != n:
        num+=1
        if '666' in str(num):
            count += 1
            
    return num

print(number(n))
