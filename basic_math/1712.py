'''
고정비용 가변비용 판매금액

총수입 = 판매금액 x 판매량
총비용 = 고정비용 + 가변비용 x 판매량
총 수입 > 총비용이 되는 판매량

'''
a, b, c = map(int, input().split())
if c-b > 0:
    print(a//(c-b)+1)
else:
    print(-1)
