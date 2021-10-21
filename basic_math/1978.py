int(input())
arr = list(map(int, input().split()))
dec = list(range(2, max(arr)+1))

# 소수 배열 만들기
i = 0
while i < len(dec):
    j = i+1
    while j < len(dec):
        if dec[j]% dec[i] == 0:
            dec.remove(dec[j])
        else:
            j+=1
    i+=1
print(len(set(arr)&set(dec)))
