'''
3이나 5로 나누어 떨어지지 않을 때까지 나눈다.

'''
sugar = int(input())
flag = sugar//5
remain = sugar%5
count = 0

while flag != 0:
    if remain % 3 ==0:
        count = flag + remain//3
        
        break
    else:
        flag -= 1
        remain = sugar - 5*flag
        
# 설탕 주머니가 5 주머니로는 나눌 수 없는 3의 배수인 경우
if flag == 0 and sugar % 3 == 0:
    print(sugar//3)
# 설탕 주머니가 3, 5로 나눌 수 없는 경우
elif flag == 0 and sugar % 3 != 0:
    print(-1)
# 설탕 주머니가 3, 5로 나눠진 경우
else:
    print(count)
