'''
자카드 유사도 : 교집합& / 합집합| // a,b가 모두 공집합인 경우에는 1이다.
1. 다중집합의 원소로 만들 것
2. 공백, 숫자, 특수문자가 들어있으면 버린다.
3. 대문자 소문자는 구분하지 않는다.
4. 답은 65536을 곱한 후 버림하고 정수부만 출력한다.
'''
import copy
def make_dict(s):
    dct = dict()
    for d in s:
        if d in dct:
            dct[d]+=1
        else:
            dct[d] = 1
    return dct

def solution(str1, str2):
    str1, str2 = str1.lower(),str2.lower()
    s1,s2 = [],[]
    for s in range(len(str1)-1):
        if 96 < ord(str1[s]) < 123 and 96 < ord(str1[s+1]) < 123:
            s1.append(str1[s]+str1[s+1])
    for s in range(len(str2)-1):
        if 96 < ord(str2[s]) < 123 and 96 < ord(str2[s+1]) < 123:
            s2.append(str2[s]+str2[s+1])
    if not s1 and not s2:
        return 65536
    
    d1,d2 = make_dict(s1),make_dict(s2)
    inter = dict()
    sumN = copy.deepcopy(d1)
    for d in d1:
        if d in d2:
            inter[d] = min(d1[d], d2[d])
    for d in d2:
        if d in d1:
            sumN[d] = max(d1[d], d2[d])
        else:
            sumN[d]=d2[d]
    return int(sum(inter.values())/sum(sumN.values())*65536)
