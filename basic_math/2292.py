'''
6의 등차수열
1. 방의 숫자 입력받기
2. while문으로 6의 등차수열 구현하기
3. 등차수열의 합보다 방의 숫자가 작으면 그 i를 출력
'''
room = int(input())
sumN=1 # 1에서부터 시작하니까
minRoom = 1
while sumN <room:
    sumN += 6 * minRoom
    minRoom+=1
print(minRoom)
