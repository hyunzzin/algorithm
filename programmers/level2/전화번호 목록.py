def solution(phone_book):
    # 최대한 길이가 짧고 앞자리수가 같은 숫자가 앞으로 간다.
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
