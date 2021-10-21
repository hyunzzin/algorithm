m = int(input())
n = int(input())
dec = list(range(2, n+1))

i = 0
while i < n-1:
    j = i+1
    while j < n-1:
        if dec[j]% dec[i] == 0:
            dec.remove(dec[j])
            n -=1
        else:
            j+=1
    i+=1
result = []
for i in dec:
    if i >= m:
        result.append(i)
        
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
