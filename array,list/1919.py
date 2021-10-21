# a가 97부터 시작됨을 이용
# 0보다 크면 -1을 하고
# 0이면 +1을 한다
fw = input()
sw = input()
arr = [0 for _ in range(26)]
cnt = 0
for f in fw:
    arr[ord(f)-97] += 1
for s in sw:
    temp = ord(s)-97
    if arr[temp] > 0:
        arr[temp]-=1
    else:
        cnt+=1
print(sum(arr)+cnt)
