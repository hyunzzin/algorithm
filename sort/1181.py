import sys
n = int(input())
result = []

for i in range(n):
    nums = sys.stdin.readline().rstrip()
    result.append((len(nums),nums))
    
result = list(set(result))
result.sort()
for x,y in result:
    print(y)



'''
import sys
n = int(input())
result = []
for i in range(n):
    nums = tuple(map(int,sys.stdin.readline().split()))
    result.append(nums)
result.sort()
for x,y in result:
    print(x, y)
    '''
