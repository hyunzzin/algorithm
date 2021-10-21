mul = 1
for i in range(0,3):
    mul *= int(input())

for j in range(0,10):
    print(str(mul).count(str(j)))
