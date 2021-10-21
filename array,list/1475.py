# 0-9 한세트
# 6-9는 서로 사용 가능
# 입력 0 <= N <= 1,000,000
# 0-9 배열 -> 최대 숫자만큼 숫자세트 필요
# 다솜이의 방번호를 한개씩 idx로 받아서 0-9배열에 1씩 추가
# 단, 6+9/2를 올림한 수를 각각 넣는다.
import math
n = input()
arr = [0]* 10
for i in range(len(n)):
    arr[int(n[i])]+=1
temp = math.ceil((arr[6]+arr[9])/2)
arr[6],arr[9] = temp, temp
print(max(arr))

